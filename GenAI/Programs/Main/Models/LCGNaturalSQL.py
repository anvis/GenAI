from Common.Database import get_db  # Import the method
from Common import Config

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_sql_query_chain
from langchain_core.prompts import PromptTemplate

def NaturalSQL_Gemini(text, modelName="gemini-1.5-pro"):

    db= get_db()

     # Connect LangChain to Gemini
    # Initialize Gemini model
    llm = ChatGoogleGenerativeAI(model=modelName, temperature=0)

    answer_prompt = PromptTemplate.from_template(
    """Generate an SQL query based on the given conditions and execute it to return the results.
Ensure the output includes both the SQL query and the executed results."""
)
    custom_prompt = PromptTemplate(
    input_variables=["question", "top_k", "table_info"],
    template="Using the following table schema:\n{table_info}\nGenerate an SQL query to answer: {input}\nReturn the top {top_k} results."
)
   

    # Create SQL query chain
    query_chain = create_sql_query_chain(llm, db, prompt=custom_prompt)

    # Ask a question
    response = query_chain.invoke({"question": text})
    print("Response from Gemini:")
    print(response)
    return response

#NaturalSQL_Gemini()
