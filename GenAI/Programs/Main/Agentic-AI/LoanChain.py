
from langchain_core.runnables import RunnableLambda
from LoanAssist.Eligibility import LoanEligibilityChecker

from langchain_google_genai import ChatGoogleGenerativeAI

import os
from getpass import getpass

from typing import Dict


# Define environment variables
#os.environ["GOOGLE_API_KEY"] = getpass("AIzaSyAx3V4SgE2KCjrGQ37iyvkCevFnrkIhA8w")
os.environ["GOOGLE_API_KEY"] = getpass("AIzaSyCl6tQ6NUrPDLtav7_JOF5Vmy9x4gfPt20")
os.environ["LANGCHAIN_API_KEY"] = getpass("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")
#os.environ["GITHUB_PERSONAL_ACCESS_TOKEN"] = getpass("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")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] =os.path.join(
    os.path.dirname(__file__), "../../Resources/googleCreds.json")
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.0.0"

GOOGLE_API_KEY = "AIzaSyCl6tQ6NUrPDLtav7_JOF5Vmy9x4gfPt20"



def get_Gemini_ChatModel(modelName="gemini-2.0-flash"):
    # Initialize Gemini model
    llm = ChatGoogleGenerativeAI(model=modelName, temperature=0,max_tokens=None)
    return llm



gemini_llm = get_Gemini_ChatModel("gemini-2.0-flash")

def explain_eligibility(result: Dict) -> str:
    if result["eligible"]:
        return "You're eligible for the loan based on your profile. Let's explore offers!"
    else:
        reasons = "\n".join(f"- {r}" for r in result["reasons"])
        return f"Unfortunately, you're not eligible due to:\n{reasons}"

eligibility_explainer = RunnableLambda(lambda result: gemini_llm.invoke(explain_eligibility(result)))

from langchain_core.runnables import RunnableSequence

loan_agent_chain = RunnableSequence(
    LoanEligibilityChecker(),
    eligibility_explainer()
)

###############

user_data = {
    "income": 28000,
    "credit_score": 680,
    "employment_type": "salaried",
    "age": 25,
    "loan_burden_ratio": 0.35
}

##response = loan_agent_chain.invoke(user_data)
##print(response)