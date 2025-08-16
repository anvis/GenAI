
import streamlit as st

st.title("🧠 LLM Chat Assistant")

prompt = st.text_input("Enter your question or prompt:")

if st.button("Generate Response"):
    st.write("Processing your prompt...")

st.markdown("**LLM Response:** This will appear bold.")

with st.sidebar:
    st.markdown("## Settings")
    model = st.selectbox("Choose Model", ["gpt-3.5-turbo", "gpt-4"])

if "history" not in st.session_state:
    st.session_state["history"] = []

st.session_state["history"].append("User prompt")

st.success("LLM response generated successfully!")
st.error("It just a fake error")
st.warning("Please pay attention to the warning")