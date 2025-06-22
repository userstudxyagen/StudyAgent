import streamlit as st
from pdf_tools import process_pdf
from web_tools import process_website
from math_tools import solve_math
from ai_tools import ask_ai

st.set_page_config(page_title="📚 StudyBot", layout="wide")
st.title("📚 StudyBot für dein Studium")

option = st.sidebar.selectbox("Funktion auswählen", [
    "🧠 Frage beantworten",
    "📄 PDF analysieren",
    "🌐 Website analysieren",
    "🧮 Mathehilfe",
    "👨‍💻 Codinghilfe"
])

if option == "🧠 Frage beantworten":
    query = st.text_area("Frage:")
    if st.button("Antwort generieren"):
        st.success(ask_ai(query))

elif option == "📄 PDF analysieren":
    file = st.file_uploader("PDF hochladen", type=["pdf"])
    question = st.text_input("Frage zur PDF:")
    if st.button("Analysieren") and file:
        st.success(process_pdf(file, question))

elif option == "🌐 Website analysieren":
    url = st.text_input("Website-URL:")
    question = st.text_input("Frage zur Website:")
    if st.button("Analysieren"):
        st.success(process_website(url, question))

elif option == "🧮 Mathehilfe":
    expr = st.text_input("Mathematischer Ausdruck:")
    if st.button("Berechnen"):
        st.code(solve_math(expr))

elif option == "👨‍💻 Codinghilfe":
    code_question = st.text_area("Codefrage:")
    if st.button("Antwort generieren"):
        st.code(ask_ai(code_question))  