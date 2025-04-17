# 🧠 Classification Projects Portfolio

Welcome to my curated collection of **classification machine learning projects**, covering diverse real-world applications such as **loan risk detection**, **customer churn**, **email spam**, and **employee attrition**.  
Each project includes **modular code**, **Streamlit dashboards**, and **well-documented training pipelines** to demonstrate practical ML development and deployment.

---

## 📁 Repository Structure

Each folder is a standalone classification project with its own dataset, modeling code, Streamlit app, and README:

```
classification_projects/
├── Classification_loan_default_risk_project/
├── classificaiton_customer_churn_prediction/
├── classification_email_spam_detection_project/
└── classification_employee_attrition_prediction/
```

---

## 🚀 Project Overviews

### 🔐 [Loan Default Risk Prediction](./Classification_loan_default_risk_project)
- Binary classification to predict loan repayment default
- Feature engineering, scaling, and ensemble modeling (RandomForest/XGBoost)
- Includes model interpretability using SHAP
- Streamlit app for borrower risk scoring

### 🔁 [Customer Churn Prediction](./classificaiton_customer_churn_prediction)
- Predicts if a customer is likely to churn based on usage, contract, and demographics
- Logistic Regression, Decision Tree, and XGBoost models
- SMOTE for class imbalance, GridSearch for tuning
- Streamlit UI for churn prediction

### 📧 [Email Spam Detection](./classification_email_spam_detection_project)
- NLP-based binary classifier for spam vs. ham emails
- Text preprocessing, TF-IDF vectorization, Naïve Bayes & Logistic Regression
- Model evaluation with Precision, Recall, F1-score
- Simple UI to test your own email text

### 👨‍💼 [Employee Attrition Prediction](./classification_employee_attrition_prediction)
- HR analytics project to predict attrition risk
- Exploratory Data Analysis with Seaborn, CatBoost model training
- Model evaluation and deployment-ready Streamlit UI
- Feature importance for HR decisions

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
📧 Email: amit@example.com  
🔗 [LinkedIn](https://www.linkedin.com/in/amitkharche)

---

## 📄 License

All content in this repository is licensed under the MIT License.  
You're welcome to fork, use, or contribute!

---

## 🙌 Feedback & Collaboration

If you find this useful, give it a ⭐  
Pull requests and suggestions are highly appreciated!
