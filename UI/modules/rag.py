
import chromadb
from sentence_transformers import SentenceTransformer, CrossEncoder

from modules import finetuned_qwen

CHROMA_PATH = ("/content/drive/MyDrive/data_handling_and_machine_learning/chroma_db")

COLLECTION_NAME = "investiq_rag"

_embedding_model = None
_reranker = None
_collection = None


def load_rag_components():
    global _embedding_model
    global _reranker
    global _collection

    if _embedding_model is None:
        _embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    if _reranker is None:
        _reranker = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

    if _collection is None:
        chroma_client = chromadb.PersistentClient(
            path=CHROMA_PATH
        )

        _collection = chroma_client.get_collection(
            name=COLLECTION_NAME
        )

    return _embedding_model, _reranker, _collection


def retrieve_chunks(
    query,
    n_candidates=10,
    n_results=5,
    company=None
):
    embedding_model, reranker, collection = load_rag_components()

    query_embedding = embedding_model.encode(
        query
    ).tolist()

    if company is not None:
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=n_candidates,
            where={"company": company}
        )
    else:
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=n_candidates
        )

    candidates = []

    for document, metadata, distance in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    ):
        candidates.append({
            "text": document,
            "metadata": metadata,
            "distance": distance
        })

    candidate_pairs = [
        (query, result["text"])
        for result in candidates
    ]

    scores = reranker.predict(candidate_pairs)

    reranked = []

    for result, score in zip(candidates, scores):
        reranked.append({
            "text": result["text"],
            "metadata": result["metadata"],
            "distance": result["distance"],
            "reranker_score": float(score)
        })

    reranked.sort(
        key=lambda x: x["reranker_score"],
        reverse=True
    )

    return reranked[:n_results]


def build_reranked_context(retrieved_chunks):
    context_parts = []

    for rank, result in enumerate(
        retrieved_chunks,
        start=1
    ):
        metadata = result["metadata"]

        context_parts.append(
            f"""
Source ID: {metadata["chunk_id"]}
Company: {metadata["company"]}
Section: {metadata["section"]}
Retrieval Rank: {rank}

Text:
{result["text"]}
"""
        )

    return "\n".join(context_parts)


def generate_response(question, company=None):
    reranked_results = retrieve_chunks(
        query=question,
        n_candidates=10,
        n_results=5,
        company=company
    )

    reranked_context = build_reranked_context(
        reranked_results
    )

    rag_prompt_v2 = f"""
You are an investment research assistant.

Answer the user's question using ONLY the retrieved source context below.

GROUNDING RULES:
1. Treat the retrieved context as the complete evidence boundary.
2. Use only information explicitly supported by the retrieved context.
3. Do not use outside knowledge to fill missing information.
4. If the context does not contain enough evidence to answer the question,
   explicitly state that the available sources do not provide enough information.
5. Cite a source ID only when the answer uses a factual detail supported by that source.
6. Do not cite a source merely because it was included in the retrieved context.
7. Do not cite irrelevant sources.
8. Never invent source IDs.
9. Every cited source ID must appear in the retrieved context.
10. Keep the answer concise and directly related to the user's question.

Return ONLY valid JSON using exactly this structure:

{{
  "answer": "A concise grounded answer.",
  "sources": ["source_id_1", "source_id_2"]
}}

User question:
{question}

Retrieved context:
{reranked_context}
"""

    response = finetuned_qwen.generate_response(
        rag_prompt_v2
    )

    return {
        "answer": response,
        "sources": [
            {
                "chunk_id": result["metadata"]["chunk_id"],
                "company": result["metadata"]["company"],
                "section": result["metadata"]["section"],
                "reranker_score": result["reranker_score"]
            }
            for result in reranked_results
        ]
    }

