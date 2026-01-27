import streamlit as st
from llm_quiz_generator import generate_single_question

st.title("Test Génération Quiz via Gemini")

st.write("Génération d'une question simple...")

question = generate_single_question(
    diploma="CAP Boucher",
    theme="Hygiène alimentaire",
    difficulty="novice",
)

if question:
    st.success("✓ Question générée !")
    st.json(question)
else:
    st.error("✗ Erreur génération")
