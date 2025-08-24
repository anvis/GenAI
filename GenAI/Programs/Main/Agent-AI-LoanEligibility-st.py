
import streamlit as st
#from Agent-AI-LoanEligibility import check_eligibility, explain_decision

st.title("Auto Loan Eligibility Agent")

income = st.number_input("Monthly Income (₹)", min_value=10000)
credit_score = st.number_input("Credit Score", min_value=300, max_value=900)
employment_type = st.selectbox("Employment Type", ["salaried", "self-employed"])
vehicle_type = st.selectbox("Vehicle Type", ["hatchback", "sedan", "SUV"])
loan_amount = st.number_input("Loan Amount (₹)", min_value=50000)

if st.button("Check Eligibility"):
    data = {
        "income": income,
        "credit_score": credit_score,
        "employment_type": employment_type,
        "vehicle_type": vehicle_type,
        "loan_amount": loan_amount
    }
    result, reason = check_eligibility(data)
    explanation = explain_decision(data, result, reason)
    st.write(explanation)
