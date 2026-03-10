import streamlit as st
from prediction_helper import predict

st.title("Lauki Finance: Credit Risk Modeling")

st.header("Enter Applicant Details")

# ---- Row 1 ----
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100)

with col2:
    income = st.number_input("Income")

with col3:
    loan_amount = st.number_input("Loan Amount")


# ---- Row 2 ----
col4, col5, col6= st.columns(3)

with col4:
    Loan_to_income_ratio = st.number_input("Loan to Income Ratio")
    
with col5:
    loan_tenure_months = st.number_input("Loan Tenure (Months)")

with col6:
    avg_dpd_per_delinquency = st.number_input("Avg DPD (Days Past Due)")
    
# ---- Row 2 ----
col7, col8, col9= st.columns(3)

with col7:
    delinquency_ratio = st.number_input("Delinquency Ratio")

with col8:
    credit_utilization_ratio = st.number_input(
        "Credit Utilization Ratio", min_value=0.0, max_value=1.0
    )

with col9:
    num_open_accounts = st.number_input("Open Loan Amounts")

# ---- Row 3 ----
col10, col11, col12 = st.columns(3)

with col10:
    residence_type = st.selectbox(
        "Residence Type",
        ["Owned", "Rented", "Mortgage"]
    )

with col11:
    loan_purpose = st.selectbox(
        "Loan Purpose",
        ["Education", "Home", "Auto", "Personal"]
    )

with col12:
     loan_type = st.selectbox(
        "Loan Type",
        ["Unsecured", "Secured"]
    )


# ---- Prediction Button ----
if st.button("Predict Credit Risk"):
    
   probability, credit_score, rating = predict(
    age,
    income,
    loan_amount,
    loan_tenure_months,
    avg_dpd_per_delinquency,
    delinquency_ratio,
    credit_utilization_ratio,
    num_open_accounts,
    residence_type,
    loan_purpose,
    loan_type
   )
   st.write(f"Deafult Probability: {probability}")
   st.write(f"Credit Score: {credit_score}")
   st.write(f"Rating : {rating}")



st.success("Prediction logic will go here.")