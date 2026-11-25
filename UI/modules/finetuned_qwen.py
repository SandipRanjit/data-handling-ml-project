
import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

BASE_MODEL_NAME = "Qwen/Qwen2.5-1.5B-Instruct"

ADAPTER_PATH = ("/content/drive/MyDrive/data_handling_and_machine_learning/week_04/outputs/Finetuned_version01/InvestIQ_finetuned_adapter_updated")

_tokenizer = None
_model = None

def load_model():
    global _tokenizer, _model

    if _tokenizer is None:

        _tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_NAME)
        _tokenizer.pad_token = _tokenizer.eos_token

    if _model is None:

        base_model = AutoModelForCausalLM.from_pretrained(
            BASE_MODEL_NAME,
            device_map="cuda",
            torch_dtype=torch.float16
        )

        base_model.config.use_cache = True

        _model = PeftModel.from_pretrained(
            base_model,
            ADAPTER_PATH
        )

        _model.eval()

    return _tokenizer, _model

def generate_response(question):
    tokenizer, model = load_model()

    messages = [
        {
            "role": "system",
            "content": (
                "You are InvestIQ, an AI investment research assistant. "
                "Explain financial metrics accurately using the definitions "
                "used by the system. Do not invent information or confuse "
                "related financial metrics."
            )
        },
        {
            "role": "user",
            "content": question
        }
    ]

    inputs = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors="pt"
    ).to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=300,
            do_sample=False
        )

    input_length = inputs["input_ids"].shape[-1]

    response = tokenizer.decode(
        outputs[0][input_length:],
        skip_special_tokens=True
    )

    return response
