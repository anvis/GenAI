from langchain.prompts import PromptTemplate
from  Models.llm import get_Gemini_model


user_data = {
    "income": 75000,
    "credit_score": 450,
    "employment_type": "salaried",
    "vehicle_type": "SUV",
    "loan_amount": 1000000  # ₹10 Lakhs
}

def check_eligibility(data):
    if data["income"] < 30000:
        return False, "Income too low"
    if data["credit_score"] < 650:
        return False, "Credit score below threshold"
    if data["loan_amount"] > data["income"] * 20:
        return False, "Requested loan exceeds income-based limit"
    return True, "Eligible"

llm = get_Gemini_model("gemini-2.0-flash")

def explain_decision(data, result, reason):
    prompt = PromptTemplate.from_template(
        "A customer with income ₹{income}, credit score {credit_score}, employment type {employment_type}, and vehicle type {vehicle_type} applied for an auto loan of ₹{loan_amount}. The system determined: {result}. Reason: {reason}. Write a friendly explanation for the customer."
    )
    return llm.invoke(prompt.format(**data, result="Eligible" if result else "Not Eligible", reason=reason))

from langchain.agents import Tool, initialize_agent

def loan_tool(query):
    # Simulate parsing query into structured data
    data = user_data  # Replace with actual parsing logic
    result, reason = check_eligibility(data)
    explanation = explain_decision(data, result, reason)
    return explanation

tools = [Tool(name="LoanEligibilityTool", func=loan_tool, description="Checks auto loan eligibility and explains the decision")]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description")
response = agent.invoke("Check auto loan eligibility for ₹10 Lakhs")
print(response)