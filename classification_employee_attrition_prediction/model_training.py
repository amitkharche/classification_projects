
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("employee_data.csv")

# Data Cleaning
df.dropna(inplace=True)

# Target Encoding
y = df["Attrition"].map({"Yes": 1, "No": 0})
X = df.drop(columns=["Attrition"])

# Feature Selection
numeric_features = ["Age", "Education", "JobSatisfaction", "MonthlyIncome", "TotalWorkingYears", "YearsAtCompany"]
categorical_features = [col for col in X.columns if col not in numeric_features]

# Preprocessing
preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
])

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# Model Training
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42))
])
pipeline.fit(X_train, y_train)

# Model Evaluation
y_pred = pipeline.predict(X_test)
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Save Model and Features
joblib.dump(pipeline, "attrition_model.pkl")
joblib.dump(X.columns.tolist(), "attrition_features.pkl")
print("\nModel and features saved successfully.")

