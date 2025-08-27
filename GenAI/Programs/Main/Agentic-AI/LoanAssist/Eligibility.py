
# agent/logic.py (snippet)

ELIGIBILITY_RULES = {
    "min_income": 30000,
    "min_credit_score": 700,
    "employment_types": ["salaried", "self-employed"],
    "age_range": (21, 60),
    "max_loan_burden_ratio": 0.4
}

from langchain_core.runnables import Runnable
from typing import Dict

class LoanEligibilityChecker(Runnable):
    def invoke(self, user_data: Dict) -> Dict:
        result = {"eligible": True, "reasons": []}

        # Rule checks
        if user_data["income"] < ELIGIBILITY_RULES["min_income"]:
            result["eligible"] = False
            result["reasons"].append("Income below minimum threshold.")

        if user_data["credit_score"] < ELIGIBILITY_RULES["min_credit_score"]:
            result["eligible"] = False
            result["reasons"].append("Credit score too low.")

        if user_data["employment_type"] not in ELIGIBILITY_RULES["employment_types"]:
            result["eligible"] = False
            result["reasons"].append("Unsupported employment type.")

        if not (ELIGIBILITY_RULES["age_range"][0] <= user_data["age"] <= ELIGIBILITY_RULES["age_range"][1]):
            result["eligible"] = False
            result["reasons"].append("Age outside eligible range.")

        if user_data["loan_burden_ratio"] > ELIGIBILITY_RULES["max_loan_burden_ratio"]:
            result["eligible"] = False
            result["reasons"].append("Loan burden exceeds allowed ratio.")

        return result