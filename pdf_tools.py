from PyPDF2 import PdfReader
from ai_tools import ask_ai

def process_pdf(uploaded_file, question):
    # PdfReader braucht ein File-like Objekt, Streamlit liefert das
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    # Prompt für AI erstellen
    prompt = f"Beantworte die folgende Frage basierend auf dem PDF Text:\n{text[:3000]}\n\nFrage: {question}"
    return ask_ai(prompt) // look at issue and code and tell the conflict and the way to solve correctly and with out any further isssues