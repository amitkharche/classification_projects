
# 🏦 Loan Default Risk Prediction

## 🎯 Business Objective
This project helps lending institutions identify borrowers who are at risk of defaulting (Charged Off). By analyzing applicant details such as loan amount, income, credit grade, and purpose, the model predicts the likelihood of a loan being paid or defaulted.

## ✅ Features Used
- loan_amnt
- term
- int_rate
- installment
- grade
- emp_length
- home_ownership
- annual_inc
- purpose
- dti

## ⚙️ Pipeline Components in `model_training.py`
- ✅ Data Cleaning
- ✅ Feature Selection
- ✅ Preprocessing Setup
- ✅ Train/Test Split
- ✅ Model Training (RandomForestClassifier)
- ✅ Model Evaluation (classification report)
- ✅ Model Saving
- ✅ Logging

## 🧪 How to Use

### 1. Train the Model
```
pip install -r requirements.txt
python model_training.py
```

### 2. Launch the Streamlit App
```
streamlit run app.py
```

### 3. Upload New Borrower Data
- Use a CSV structured like `loan_data.csv`
- Get predictions for loan default risk
- Download results from the app

## 📁 Files Included
- loan_data.csv
- model_training.py
- app.py
- loan_model.pkl
- loan_features.pkl
- requirements.txt
- README.md
