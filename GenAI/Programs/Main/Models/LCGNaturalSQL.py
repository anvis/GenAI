from Common.Database import get_db  # Import the method
from Common import Config

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_sql_query_chain

def NaturalSQL_Gemini(text, modelName="gemini-1.5-pro"):

    db= get_db()

    # Connect LangChain to Gemini
    # Initialize Gemini model
    llm = ChatGoogleGenerativeAI(model=modelName, temperature=0)

    # Create SQL query chain
    query_chain = create_sql_query_chain(llm, db)

    # Ask a question
    response = query_chain.invoke({"question": text})
    print(response)
    return response

#NaturalSQL_Gemini()
