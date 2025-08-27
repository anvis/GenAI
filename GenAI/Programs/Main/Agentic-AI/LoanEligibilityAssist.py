import streamlit as st
from LoanChain import loan_agent_chain

st.set_page_config(page_title="Loan Eligibility Assistant", layout="centered")
st.title("💰 Conversational Loan Assistant")

st.markdown("Fill in your details to check loan eligibility:")

# 🧾 User Input Form
with st.form("loan_form"):
    income = st.number_input("Monthly Income (₹)", min_value=0, step=1000)
    credit_score = st.number_input("Credit Score", min_value=300, max_value=900)
    employment_type = st.selectbox("Employment Type", ["salaried", "self-employed"])
    age = st.slider("Age", min_value=18, max_value=65)
    loan_burden_ratio = st.slider("Existing Loan Burden (% of income)", min_value=0.0, max_value=1.0, step=0.01)

    submitted = st.form_submit_button("Check Eligibility")

# 🧠 Agent Response
if submitted:
    user_data = {
        "income": income,
        "credit_score": credit_score,
        "employment_type": employment_type,
        "age": age,
        "loan_burden_ratio": loan_burden_ratio
    }

    with st.spinner("Analyzing your profile..."):
        response = loan_agent_chain.invoke(user_data)

    st.success("Here's what the assistant says:")
    st.markdown(response.content if hasattr(response, "content") else response)