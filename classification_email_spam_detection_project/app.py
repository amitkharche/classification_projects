
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="📧 Email Spam Detection", layout="centered")
st.title("📬 Email Spam Detection")

# Load trained model
model = joblib.load("spam_classifier_model.pkl")
features = joblib.load("spam_features.pkl")

uploaded_file = st.file_uploader("📤 Upload email data (CSV)", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    prediction = model.predict(df['EmailContent'])
    df['Prediction'] = prediction
    df['Prediction'] = df['Prediction'].map({1: 'Spam', 0: 'Not Spam'})
    st.subheader("📋 Prediction Results")
    st.write(df.head())
    st.download_button("📥 Download Predictions", df.to_csv(index=False), "email_spam_predictions.csv")
