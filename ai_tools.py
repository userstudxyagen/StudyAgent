import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("HF_TOKEN")

client = InferenceClient(model="mistralai/Mixtral-8x7B-Instruct-v0.1", token=token)

def ask_ai(prompt):
    try:
        return client.text_generation(prompt=prompt, max_new_tokens=512)
    except Exception as e:
        return f"Fehler: {e}"