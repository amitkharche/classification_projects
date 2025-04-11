import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("email_spam_data.csv")

# Data Cleaning
df.dropna(inplace=True)

# Feature Selection
X = df['EmailContent']  # Feature: Email Content
y = df['IsSpam']        # Target: Spam or Not Spam

# Preprocessing setup: TF-IDF vectorizer
tfidf = TfidfVectorizer(stop_words='english', max_features=500)

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training pipeline
pipeline = Pipeline([
    ('vectorizer', tfidf),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced'))
])
pipeline.fit(X_train, y_train)

# Model Evaluation
y_pred = pipeline.predict(X_test)
print("\nClassification Report:\n", classification_report(y_test, y_pred, zero_division=1))

# Save Model
joblib.dump(pipeline, "spam_classifier_model.pkl")

# Save TF-IDF feature names
feature_names = pipeline.named_steps['vectorizer'].get_feature_names_out().tolist()
joblib.dump(feature_names, "spam_features.pkl")

print("Model and features saved successfully.")
