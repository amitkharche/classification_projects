
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-orange)


# 📧 Email Spam Detection

## 🎯 Business Use Case
Email spam detection is crucial for filtering unwanted emails. By detecting spam emails, organizations can save time and resources while protecting users from phishing or malicious activities. This project uses machine learning to classify emails as spam or not.

## 🧠 Features Used
- Email content (text) transformed into numerical features using **TF-IDF** vectorization.
- Class label: **Spam (1)** or **Not Spam (0)**.

## ⚙️ What's in `model_training.py`
- ✅ Data Cleaning
- ✅ Feature Selection
- ✅ Preprocessing Setup
- ✅ Train/Test Split
- ✅ Model Training (RandomForestClassifier)
- ✅ Model Evaluation (classification report)
- ✅ Model Saving
- ✅ Printing/Logging

## 🧪 How to Use

### 1. Train the Model
```
pip install -r requirements.txt
python model_training.py
```

### 2. Run Streamlit App
```
streamlit run app.py
```

### 3. Upload Email Data for Prediction
- Upload a CSV file with email content similar to `email_spam_data.csv`
- View and download the spam detection results

## 📁 Files Included
- email_spam_data.csv
- model_training.py
- app.py
- spam_classifier_model.pkl
- requirements.txt
- README.md
