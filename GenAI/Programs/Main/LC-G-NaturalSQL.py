import streamlit as st
from Models.LCGNaturalSQL import NaturalSQL_Gemini
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain.chains.base import Chain
import pandas as pd
import re
import json


st.title('Natural Language to SQL using Langchain and Gemini')

def preprocess_text(processed_text):
    """Example preprocessing method."""
    print(f"Preprocessing: {processed_text}")
    return NaturalSQL_Gemini(processed_text)  # Ensure this returns a value

def generate_response(text):
    """Example response generator."""
    print(f"Generating response for: {text}")
    return f"Processed input: {text}"    

# Wrap functions in RunnableLambda
preprocessor = RunnableLambda(preprocess_text)
response_generator = RunnableLambda(generate_response)

# Define prompt template
prompt = PromptTemplate.from_template("{processed_text}")

# Create a simple chain
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

# Input prompt
user_prompt = st.text_input("Enter your prompt:", "")

def structure_UI(output):
    match = re.search(r"SQLResult:\n```\n([\s\S]+?)\n```", output["response"])
    if match:
        sql_result_text = match.group(1)

        # Convert SQLResult to a structured format
        rows = [line.split("\t") for line in sql_result_text.strip().split("\n")]
        columns = rows.pop(0)  # First row contains column names
        df = pd.DataFrame(rows, columns=columns)

        # Display in Streamlit UI
        #st.title("Extracted SQLResult")
      #  st.dataframe(df)

        with st.expander("SQLResult"):
            st.write(df)

        st.success("sSQLResult extracted and displayed successfully! 🚀")
    else:
        st.error("SQLResult not found in response.")


# Run the chain
if user_prompt:
    # Execute the chain
    chain = CustomChain()
    output = chain.invoke({"processed_text": user_prompt})
    #st.write(output)  # Display the output in Streamlit
    structure_UI(output)  # Display the structured SQLResult
    




"""
    df = pd.DataFrame(output["response"])

    for index, row in df.iterrows():
        with st.expander(f"Row {index + 1}"):
            for col in df.columns:
                st.write(f"**{col}:** {row[col]}")
            st.write("---")  # Separator for clarity

   
    with st.expander("Processed_text"):
     st.write(output["Processed_text"])

    with st.expander("Skills"):
     st.write(output["skills"])

    with st.expander("Projects"):
     st.write(output["Projects"])
     """