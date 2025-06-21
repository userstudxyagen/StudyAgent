import fitz
from utils.ai_tools import ask_ai

def process_pdf(uploaded_file, question):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = "".join([page.get_text() for page in doc])
    prompt = f"Antworte auf die Frage auf Basis dieses Textes:\n{text[:3000]}\n\nFrage: {question}"
    return ask_ai(prompt)