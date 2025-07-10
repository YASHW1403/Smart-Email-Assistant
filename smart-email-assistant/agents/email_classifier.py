import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import os

df = pd.read_csv("data/emails.csv")

X = df["email_text"]
y = df["category"]

vectorizer = TfidfVectorizer()
X_vect = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("📊 Classification Report:\n", classification_report(y_test, y_pred))
print("🔢 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("🎯 Accuracy:", accuracy_score(y_test, y_pred))

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/email_classifier.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("✅ Model and vectorizer saved to 'models/'")

def predict_category(email_text):
    model = joblib.load("models/email_classifier.pkl")
    vectorizer = joblib.load("models/vectorizer.pkl")
    X_input = vectorizer.transform([email_text])
    proba = model.predict_proba(X_input)[0]
    predicted_index = proba.argmax()
    predicted_label = model.classes_[predicted_index]
    confidence = proba[predicted_index]

    return {
        "email_text": email_text,
        "predicted_category": predicted_label,
        "confidence": round(confidence, 2)
    }