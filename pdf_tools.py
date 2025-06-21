from PyPDF2 import process_pdf
from ai_tools import ask_ai

def process_pdf(uploaded_file, question):
    try:
        reader = PdfReader(uploaded_file)
        text = " ".join(
            page.extract_text()
            for page in reader.pages
            if page.extract_text()
        )
        prompt = (
            f"Antworte auf die Frage auf Basis dieses PDF-Textes:\n"
            f"{text[:3000]}\n\nFrage: {question}"
        )
        return ask_ai(prompt)
    except Exception as e:
        return f"Fehler beim PDF-Verarbeiten: {e}"
