
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-orange)


# 👨‍💼 Employee Attrition Prediction

## 🎯 Business Use Case
Organizations lose valuable time and resources due to employee attrition. This project predicts which employees are likely to leave (Attrition = Yes), helping HR departments take proactive steps to retain top talent.

## 🧠 Features Used
- Age
- Department
- Job Role
- Education Level
- Job Satisfaction
- Monthly Income
- Total Working Years
- Years at Company
- Overtime Status

## ⚙️ What's in `model_training.py`
- ✅ Data Cleaning
- ✅ Feature Selection
- ✅ Preprocessing Setup
- ✅ Train/Test Split
- ✅ Model Training (RandomForestClassifier)
- ✅ Model Evaluation (classification report)
- ✅ Model Saving
- ✅ Logging via print()

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

### 3. Upload CSV File
- Upload employee data (same format as `employee_data.csv`)
- View and download attrition predictions

## 📁 Files Included
- employee_data.csv
- model_training.py
- app.py
- attrition_model.pkl
- attrition_features.pkl
- requirements.txt
- README.md
