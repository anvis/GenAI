from langchain_google_genai import ChatGoogleGenerativeAI
from Common import Config

def get_Gemini_model(modelName="gemini-1.5-pro"):
    # Initialize Gemini model
    llm = ChatGoogleGenerativeAI(model=modelName, temperature=0)
    return llm