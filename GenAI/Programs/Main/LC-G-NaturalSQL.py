import streamlit as st
from Models.LCGNaturalSQL import NaturalSQL_Gemini
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain.chains.base import Chain


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

# Run the chain
if user_prompt:
    # Execute the chain
    chain = CustomChain()
    output = chain.invoke({"processed_text": user_prompt})
    st.write(output)  # Display the output in Streamlit