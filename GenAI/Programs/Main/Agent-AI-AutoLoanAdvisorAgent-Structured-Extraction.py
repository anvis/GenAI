
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from  Models.llm import get_Gemini_model
from langchain.prompts import PromptTemplate

class UserProfile(BaseModel):
    income: int = Field(..., description="Monthly income in INR")
    credit_score: int = Field(..., description="Credit score")
    car_model: str = Field(..., description="Desired car model")

parser = PydanticOutputParser(pydantic_object=UserProfile)

extraction_prompt = PromptTemplate.from_template("""
Extract the following fields from the user's input:
- Monthly income (INR)
- Credit score
- Car model

User input:
{user_input}

{format_instructions}
""")


llm = get_Gemini_model("gemini-2.0-flash")

user_input = "I earn ₹45,000 monthly, have a credit score of 720, and want a loan for a Maruti Swift."

print(parser.get_format_instructions())

formatted_prompt = extraction_prompt.format(
    user_input=user_input,
    format_instructions=parser.get_format_instructions()
)

structured_profile = llm.invoke(formatted_prompt)
parsed_profile = parser.parse(structured_profile.content)
print("parsed_profile")
print(parsed_profile)

##--


from langchain.vectorstores import FAISS
from langchain.embeddings import GoogleGenerativeAIEmbeddings
from langchain.schema import Document

embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

loan_docs = [
    Document(page_content=p["description"], metadata=p)
    for p in loan_products
]

vector_store = FAISS.from_documents(loan_docs, embedding_model)
#-----
query = f"Auto loan for someone earning ₹{parsed_profile.income}, credit score {parsed_profile.credit_score}, wants a {parsed_profile.car_model}"
results = vector_store.similarity_search(query, k=2)

for r in results:
    print(f"Matched: {r.metadata['name']} — {r.page_content}")


#----


recommendation_prompt = PromptTemplate.from_template("""
You are an Auto Loan Advisor Agent.

User Profile:
Income: ₹{income}
Credit Score: {credit_score}
Car Model: {car_model}

Top Matching Loan Products:
{loan_matches}

Recommend the best product and explain why.
""")

loan_matches = "\n".join([f"{r.metadata['name']}: {r.page_content}" for r in results])

final_prompt = recommendation_prompt.format(
    income=parsed_profile.income,
    credit_score=parsed_profile.credit_score,
    car_model=parsed_profile.car_model,
    loan_matches=loan_matches
)

response = llm.invoke(final_prompt)
print(response.content)

