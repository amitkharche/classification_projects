# 🧠 Classification Projects Portfolio

Welcome to my curated collection of **classification machine learning projects**, covering diverse real-world applications such as **loan risk detection**, **customer churn**, **email spam**, and **employee attrition**.  
Each project includes **modular code**, **Streamlit dashboards**, and **well-documented training pipelines** to demonstrate practical ML development and deployment.

---

## 📁 Repository Structure

Each folder is a standalone classification project with its own dataset, modeling code, Streamlit app, and README:

```
classification_projects/
├── Classification_loan_default_risk_project/
├── classification_customer_churn_prediction/
├── classification_email_spam_detection_project/
└── classification_employee_attrition_prediction/
```

---

## 🚀 Project Overviews

### 🔐 [Loan Default Risk Prediction](./Classification_loan_default_risk_project)
- Predicts loan default risk using customer financial and loan profile data
- Random Forest classifier with preprocessing pipeline for scaling and encoding
- Numerical and categorical features include loan amount, interest rate, income, and debt-to-income ratio
- Model saved as a .pkl file along with feature names for deployment in Streamlit or production systems

### 🔁 [Customer Churn Prediction](./classificaiton_customer_churn_prediction)
- Predicts if a customer is likely to churn based on usage patterns, billing information, and service features
- Logistic Regression, Random Forest, and XGBoost models
- Preprocessing pipeline with scaling and one-hot encoding
- Models saved as .pkl files for deployment in Streamlit UIPredicts if a customer is likely to churn based on usage, contract, and demographics

### 📧 [Email Spam Detection](./classification_email_spam_detection_project)
- Classifies emails as spam or not spam using text-based features
- TF-IDF vectorization of email content for feature extraction
- Random Forest model trained with class weighting to handle imbalance
- Pipeline includes vectorization and classification, saved for deployment in Streamlit UI

### 👨‍💼 [Employee Attrition Prediction](./classification_employee_attrition_prediction)
- Predicts whether an employee is likely to leave the organization using HR data
- Random Forest classifier with preprocessing pipeline for scaling and one-hot encoding
- Numerical and categorical features include age, education, job satisfaction, income, and tenure
- Model saved as a .pkl pipeline and ready for deployment in a Streamlit dashboard

---

## 🛠 Tech Stack

- Python 3.8+
- Scikit-learn, XGBoost, CatBoost, LightGBM
- Pandas, NumPy, Matplotlib, Seaborn
- Streamlit for interactive dashboards
- SHAP & Lime for model explainability
- Joblib for model persistence

---

## 📦 How to Use

### 🔧 Clone the Repository

```bash
git clone https://github.com/amitkharche/classification_projects.git
cd classification_projects
```

### 📂 Navigate to Any Project

```bash
cd classification_email_spam_detection_project
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 🏋️‍♂️ Train the Model

```bash
python model_training.py
```

### 🌐 Launch Streamlit App

```bash
streamlit run app.py
```

---

## 📬 Contact

**Amit Kharche**  
🔗 [LinkedIn](https://www.linkedin.com/in/amitkharche)

---

## 📄 License

All content in this repository is licensed under the MIT License.  
You're welcome to fork, use, or contribute!

---

## 🙌 Feedback & Collaboration

If you find this useful, give it a ⭐  
Pull requests and suggestions are highly appreciated!
