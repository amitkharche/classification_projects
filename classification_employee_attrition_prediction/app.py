
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="👨‍💼 Employee Attrition Prediction", layout="centered")
st.title("🔍 HR Analytics - Attrition Classifier")

model = joblib.load("attrition_model.pkl")
features = joblib.load("attrition_features.pkl")

uploaded_file = st.file_uploader("📤 Upload employee data (CSV)", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    input_df = df[features]
    prediction = model.predict(input_df)
    df["Prediction"] = prediction
    df["Prediction"] = df["Prediction"].map({1: "Attrition", 0: "Retained"})
    st.subheader("📋 Prediction Results")
    st.write(df.head())
    st.download_button("📥 Download Predictions", df.to_csv(index=False), "employee_attrition_predictions.csv")
