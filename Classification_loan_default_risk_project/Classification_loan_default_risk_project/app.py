
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="💳 Loan Default Risk Prediction", layout="centered")
st.title("🏦 Loan Default Risk Classifier")

model = joblib.load("loan_model.pkl")
features = joblib.load("loan_features.pkl")

uploaded_file = st.file_uploader("📤 Upload borrower data (CSV)", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    input_df = df[features]
    prediction = model.predict(input_df)
    df["Prediction"] = prediction
    df["Prediction"] = df["Prediction"].map({1: "Charged Off", 0: "Fully Paid"})
    st.subheader("📋 Prediction Results")
    st.write(df.head())
    st.download_button("📥 Download Predictions", df.to_csv(index=False), "loan_predictions.csv")
