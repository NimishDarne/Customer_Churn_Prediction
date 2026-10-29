
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

# Load the saved model pipeline
MODEL_PATH = (
    Path(__file__).resolve().parent
    / "models"
    / "churn_pipeline.joblib"
)

model = joblib.load(MODEL_PATH)

# Match the threshold selected using training data
THRESHOLD = 0.6

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction")
st.write(
    "Enter customer details to estimate the probability "
    "that the customer will leave the telecom company."
)

st.info(
    "This model was trained on historical customer data. "
    "Its predictions are estimates, not guarantees."
)

with st.form("customer_form"):
    st.subheader("1. Customer Information")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox(
            "Gender", ["Female", "Male"]
        )
        senior_citizen = st.selectbox(
            "Senior citizen?", [0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No"
        )
        partner = st.selectbox(
            "Has a partner?", ["Yes", "No"]
        )
        dependents = st.selectbox(
            "Has dependents?", ["Yes", "No"]
        )
        tenure = st.slider(
            "Tenure (months)", 0, 72, 12
        )

    with col2:
        phone_service = st.selectbox(
            "Phone service", ["Yes", "No"]
        )

        multiple_lines = st.selectbox(
            "Multiple lines",
            ["No", "Yes", "No phone service"]
        )

        internet_service = st.selectbox(
            "Internet service",
            ["DSL", "Fiber optic", "No"]
        )

        contract = st.selectbox(
            "Contract type",
            ["Month-to-month", "One year", "Two year"]
        )

        paperless_billing = st.selectbox(
            "Paperless billing", ["Yes", "No"]
        )

    st.subheader("2. Internet and Additional Services")

    col3, col4 = st.columns(2)

    with col3:
        online_security = st.selectbox(
            "Online security",
            ["Yes", "No", "No internet service"]
        )
        online_backup = st.selectbox(
            "Online backup",
            ["Yes", "No", "No internet service"]
        )
        device_protection = st.selectbox(
            "Device protection",
            ["Yes", "No", "No internet service"]
        )
        tech_support = st.selectbox(
            "Tech support",
            ["Yes", "No", "No internet service"]
        )

    with col4:
        streaming_tv = st.selectbox(
            "Streaming TV",
            ["Yes", "No", "No internet service"]
        )
        streaming_movies = st.selectbox(
            "Streaming movies",
            ["Yes", "No", "No internet service"]
        )
        payment_method = st.selectbox(
            "Payment method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )

    st.subheader("3. Billing Information")

    col5, col6 = st.columns(2)

    with col5:
        monthly_charges = st.number_input(
            "Monthly charges",
            min_value=0.0,
            max_value=1000.0,
            value=70.0,
            step=1.0
        )

    with col6:
        total_charges = st.number_input(
            "Total charges",
            min_value=0.0,
            max_value=100000.0,
            value=840.0,
            step=10.0
        )

    submitted = st.form_submit_button(
        "Predict Churn",
        type="primary",
        use_container_width=True
    )


if submitted:
    errors = []

    # Check phone-service consistency
    if phone_service == "No" and multiple_lines != "No phone service":
        errors.append(
            "If Phone service is No, Multiple lines must be "
            "'No phone service'."
        )

    if phone_service == "Yes" and multiple_lines == "No phone service":
        errors.append(
            "If Phone service is Yes, choose Yes or No for "
            "Multiple lines."
        )

    # Check internet-service consistency
    internet_features = {
        "Online security": online_security,
        "Online backup": online_backup,
        "Device protection": device_protection,
        "Tech support": tech_support,
        "Streaming TV": streaming_tv,
        "Streaming movies": streaming_movies,
    }

    if internet_service == "No":
        for feature, value in internet_features.items():
            if value != "No internet service":
                errors.append(
                    f"{feature} must be 'No internet service' "
                    "when Internet service is No."
                )
    else:
        for feature, value in internet_features.items():
            if value == "No internet service":
                errors.append(
                    f"{feature} cannot be 'No internet service' "
                    "when Internet service is {internet_service}."
                )

    # Basic billing sanity checks
    if tenure == 0 and total_charges > 0:
        errors.append(
            "Total charges should be zero when tenure is zero "
            "for this demo."
        )

    if monthly_charges == 0 and total_charges > 0:
        errors.append(
            "Total charges cannot be positive when monthly "
            "charges are zero."
        )

    if errors:
        st.error("Please correct the following inputs:")
        for error in errors:
            st.write(f"- {error}")

    else:
        customer = pd.DataFrame([{
            "gender": gender,
            "SeniorCitizen": senior_citizen,
            "Partner": partner,
            "Dependents": dependents,
            "tenure": tenure,
            "PhoneService": phone_service,
            "MultipleLines": multiple_lines,
            "InternetService": internet_service,
            "OnlineSecurity": online_security,
            "OnlineBackup": online_backup,
            "DeviceProtection": device_protection,
            "TechSupport": tech_support,
            "StreamingTV": streaming_tv,
            "StreamingMovies": streaming_movies,
            "Contract": contract,
            "PaperlessBilling": paperless_billing,
            "PaymentMethod": payment_method,
            "MonthlyCharges": monthly_charges,
            "TotalCharges": total_charges
        }])

        churn_probability = model.predict_proba(customer)[0, 1]
        predicted_churn = churn_probability >= THRESHOLD

        st.divider()
        st.subheader("Prediction Result")

        
        st.metric(
            "Estimated churn probability",
            f"{churn_probability:.1%}"
        )
        st.progress(float(churn_probability))

        if churn_probability < 0.30:
            risk_category = "Low"
            st.success("Risk category: Low")
        elif churn_probability < THRESHOLD:
            risk_category = "Moderate"
            st.warning("Risk category: Moderate")
        else:
            risk_category = "High"
            st.error("Risk category: High")

        if predicted_churn:
            st.write("**Model classification:** Likely to churn")
        else:
            st.write("**Model classification:** Likely to stay")

        st.caption(
            "Risk categories are illustrative and have not been "
            "validated against business outcomes. Predictions are estimates, "
            "not guarantees."
        )


