
import streamlit as st
import json
import markdown
import re
from modules import utils
from modules import base_qwen
from modules import finetuned_qwen
from modules import rag

def initialize_chat():

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "message": (
                    "Hi! I'm your InvestIQ research assistant. "
                    "Ask me anything about the analyzed companies, "
                    "risk, sectors, or your investment strategy."
                )
            }
        ]

    if "chat_method" not in st.session_state:
        st.session_state.chat_method = "Base Qwen"

    if "chat_generating" not in st.session_state:
        st.session_state.chat_generating = False

def normalize_ai_response(response):
    """
    Convert model output into plain human-readable text
    for the Streamlit chat UI.

     Handles:
    - Plain text responses
    - Valid JSON responses containing "answer"
    - Malformed JSON produced by the fine-tuned model
    """

    if not isinstance(response, str):
        return str(response)

    response = response.strip()

    # 1. Try normal JSON parsing first
    try:
        parsed = json.loads(response)

        if isinstance(parsed, dict):

            if parsed.get("answer"):
                return str(parsed["answer"])

            if parsed.get("summary"):
                return str(parsed["summary"])

    except (json.JSONDecodeError, TypeError):
        pass

    # 2. Handle malformed JSON from Fine-Tuned Qwen
    answer_match = re.search(
        r'"answer"\s*:\s*"(.+?)"\s*,\s*"{0,2}sources"',
        response,
        re.DOTALL
    )

    if answer_match:
        return answer_match.group(1).strip()

    # 3. Fallback
    return response

def generate_chat_response(question):

    method = st.session_state.chat_method

    if method == "Base Qwen":
        response = base_qwen.generate_response(question)

        return {
            "message": normalize_ai_response(response),
            "sources": []
        }

    elif method == "Fine-Tuned Qwen":
        response = finetuned_qwen.generate_response(question)

        st.write("DEBUG FT RAW RESPONSE:", response)

        return {
            "message": normalize_ai_response(response),
            "sources": []
        }

    elif method == "RAG":
        rag_result = rag.generate_response(question)

        if isinstance(rag_result, dict):
            response = rag_result.get("answer", "")
            sources = rag_result.get("sources", [])
        else:
            response = rag_result
            sources = []

        return {
            "message": normalize_ai_response(response),
            "sources": sources
        }

    return {
        "message": "Please select an analysis method.",
        "sources": []
    }


def render_chat():

    sparkles_svg = utils.load_svg("sparkles.svg")
    user_svg = utils.load_svg("user-round.svg")
    sparkles_img = utils.load_svg_as_image("sparkles.svg")

    if (
        st.session_state.chat_generating
        and "pending_question" in st.session_state
    ):

        question = st.session_state.pending_question

        with st.spinner("Researching..."):
            result = generate_chat_response(question)

        st.session_state.messages.append({
            "role": "assistant",
            "message": result["message"],
            "sources": result.get("sources", [])
        })

        st.session_state.chat_generating = False
        del st.session_state.pending_question

        st.rerun()

    with st.container(border=True):

        st.markdown(
            f"""
            <div class="chat-header">
                <div class="chat-title">
                    AI CHAT
                </div>
                <div class="chat-badge">
                    <span class="result-icon">
                        {sparkles_svg}
                    </span>
                    AI assistant
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        for chat in st.session_state.messages:
            if chat["role"] == "user":
                st.markdown(
                    f"""
                      <div class="user-message">
                          <div class="user-bubble">
                              {chat["message"]}
                          </div>
                          <div class="user-icon">
                              {user_svg}
                          </div>
                      </div>
                    """,
                    unsafe_allow_html=True
                )

            else:
                formatted_message = markdown.markdown(chat["message"])

                st.html(
                    f"""
                    <div class="chat-message">
                        <div class="chat-icon">
                            <img src="{sparkles_img}" alt="AI">
                        </div>
                        <div class="chat-bubble">
                            {formatted_message}
                        </div>
                    </div>
                    """
                )

                sources = chat.get("sources", [])

                if sources:
                    with st.expander(f"Sources ({len(sources)})", expanded=False):

                        for i, source in enumerate(sources, start=1):

                            if isinstance(source, dict):

                                chunk_id = (
                                    source.get("chunk_id")
                                    or source.get("id")
                                    or source.get("source")
                                    or f"Source {i}"
                                )

                                section = (
                                    source.get("section")
                                    or source.get("section_name")
                                    or source.get("category")
                                    or ""
                                )

                                company = (
                                    source.get("company")
                                    or source.get("company_name")
                                    or ""
                                )

                                if company and section:
                                    label = f"{company} — {section}"

                                elif section:
                                    label = section

                                else:
                                    label = chunk_id

                                st.markdown(f"**{i}. {label}**")

                                if chunk_id:
                                    st.caption(f"Chunk: {chunk_id}")

                            else:
                                st.markdown(f"**{i}. {source}**")

        with st.form("chat_form", clear_on_submit=True):

            chat_col1, chat_col2 = st.columns([10, 1])

            with chat_col1:

                user_question = st.text_input(
                    "Ask a question",
                    placeholder="Ask about companies, risk, sectors...",
                    label_visibility="collapsed",
                )

            with chat_col2:

                send = st.form_submit_button("➤")

        st.markdown("<div style='margin-top: 12px;'></div>", unsafe_allow_html=True)

        selected_method = st.radio(
            "Analysis Method",
            [
                "Base Qwen",
                "Fine-Tuned Qwen",
                "RAG"
            ],
            horizontal=True,
            key="chat_method"
        )


        if send and user_question.strip():

            question = user_question.strip()

            st.session_state.messages.append({
                "role": "user",
                "message": question
            })

            with st.spinner("Thinking..."):
                result = generate_chat_response(question)

            st.session_state.messages.append({
                "role": "assistant",
                "message": result["message"],
                "sources": result.get("sources", [])
            })

            st.rerun()
