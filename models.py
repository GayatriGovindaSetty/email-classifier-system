import joblib
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC 
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

MODEL_PATH = "svm_email_classifier.pkl"  # Save in current directory

def train_model(csv_path: str):
    df = pd.read_csv(csv_path)
    X = df["email"]
    y = df["type"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("svm", SVC(probability=True))
    ])

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    print(classification_report(y_test, y_pred))

    joblib.dump(pipeline, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Model file not found. Train the model first.")
    return joblib.load(MODEL_PATH)

def predict_category(text: str) -> str:
    model = load_model()
    return model.predict([text])[0]

# Call training when running this file
if __name__ == "__main__":
    train_model("combined_emails_with_natural_pii.csv")