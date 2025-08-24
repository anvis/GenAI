from loanProducts import loan_products
from langchain.prompts import PromptTemplate
from  Models.llm import get_Gemini_model

template = """
You are an Auto Loan Advisor Agent. Based on the user's profile, recommend the best loan product.

User Profile:
{user_input}

Loan Products:
{loan_data}

Respond with:
- Recommended product name
- Reason for recommendation
- Any advice or alternatives
"""

prompt = PromptTemplate.from_template(template)


user_input = "I earn ₹45,000 monthly, have a credit score of 720, and want a loan for a Maruti Swift."

formatted_prompt = prompt.format(
    user_input=user_input,
    loan_data="\n".join([f"{p['name']}: {p['description']} (Min Income: {p['min_income']}, Min Credit Score: {p['min_credit_score']})" for p in loan_products])
)

llm = get_Gemini_model("gemini-2.0-flash")

response = llm.invoke(formatted_prompt)
print(response.content)