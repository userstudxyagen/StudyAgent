import requests
from bs4 import BeautifulSoup
from utils.ai_tools import ask_ai

def process_website(url, question):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        content = soup.get_text()
        prompt = f"Beantworte diese Frage auf Basis dieser Website:\n{content[:3000]}\n\nFrage: {question}"
        return ask_ai(prompt)
    except Exception as e:
        return f"Fehler beim Laden: {e}"