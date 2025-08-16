import streamlit as st

st.title("🧠 LLM Chat Assistant")

prompt = st.text_input("Enter your question or prompt:")

if st.button("Generate Response"):
    st.write("Processing your prompt...")

