import streamlit as st
from Models.LCGNaturalSQL import NaturalSQL_Gemini
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain.chains.base import Chain
import pandas as pd
import re


# Header Section
st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'> English ➡️ SQL </h1>
    <h2 style='text-align: center; color: #555;'>Transform Natural Language into SQL Queries</h2>    
    """,
    unsafe_allow_html=True
)



# Define available LLMs
llms = ["gemini-1.5-pro", "gemini-2.0-flash"]

# Sidebar for User Input
with st.sidebar:
    selected_llm = st.selectbox("Select an LLM:", llms)
    user_prompt = st.text_input("Enter your prompt:", "")
    st.button("🚀 Submit")

# Preprocessing Function
def preprocess_text(processed_text):
    """Preprocess the input text."""
    print(f"Preprocessing: {processed_text}")
    return NaturalSQL_Gemini(processed_text, selected_llm)

# Response Generation Function
def generate_response(text):
    """Generate a response for the given text."""
    print(f"Generating response for: {text}")
    return f"Processed input: {text}"

# Wrap functions in RunnableLambda
preprocessor = RunnableLambda(preprocess_text)
response_generator = RunnableLambda(generate_response)

# Define Prompt Template
prompt = PromptTemplate.from_template("{processed_text}")

# Custom Chain Class
class CustomChain(Chain):
    def _call(self, inputs):
        prompt = inputs["processed_text"]
        return {"response": preprocess_text(prompt)}

    @property
    def input_keys(self):
        return ["processed_text"]

    @property
    def output_keys(self):
        return ["response"]

# UI Structure Function
def structure_UI(output, placeholder):
    """Structure the UI to display SQL results."""
    # Define regex patterns based on placeholder
    if "SQLResult" in placeholder:
        pattern = rf"{placeholder}:?\n```\n([\s\S]+?)\n```"
    elif "sql" in placeholder:
        pattern = rf"{placeholder}\n([\s\S]+?)\n"
    elif "Answer" in placeholder:
        pattern = r"Answer:\n([\s\S]+)"

    # Extract the SQLResult using regex
    match = re.search(pattern, output["response"])
    if match:
        sql_result_text = match.group(1)

        # Convert SQLResult to a structured format
        rows = [line.split("\t") for line in sql_result_text.strip().split("\n")]
        columns = rows.pop(0)  # First row contains column names
        df = pd.DataFrame(rows, columns=columns)

        # Display in Streamlit UI
        with st.expander(placeholder):
            if "SQLResult" in placeholder:
                st.dataframe(df)
            elif "sql" in placeholder:
                st.markdown(f"<p style='color: #4CAF50; font-size: 18px;'> {sql_result_text}</p>", unsafe_allow_html=True)
            elif "Answer" in placeholder:
                st.markdown(f"<p style='color: #4CAF50; font-size: 18px;'> {sql_result_text}</p>", unsafe_allow_html=True)

# Run the Chain
if user_prompt:
    chain = CustomChain()
    output = chain.invoke({"processed_text": user_prompt})
    # Output Section Header
    st.markdown("### 📌 Output")
    structure_UI(output, "SQLResult")
    structure_UI(output, "sql")
    structure_UI(output, "Answer")

st.write("\n" * 50) 

# Footer with Branding
st.markdown("""
    <hr>
    <p style='text-align: center; color: #777;'>Natural Language to SQL using Langchain and Gemini</p>
            <p style='text-align: center; color: #777;'>This application allows you to convert natural language queries into SQL using Gemini LLM.</p>
""", unsafe_allow_html=True)