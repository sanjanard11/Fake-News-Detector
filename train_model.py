import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# Load dataset
print("Loading dataset...")

data = pd.read_csv("dataset/news.csv")

print("\nDataset Preview:")
print(data.head())


# Check for missing values
data.dropna(subset=["text", "label"], inplace=True)


# Features and labels
X = data["text"]
y = data["label"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Convert text into numerical features
print("\nCreating TF-IDF features...")

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_df=0.9
)

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)


# Train the model
print("\nTraining model...")

model = LogisticRegression(max_iter=1000)

model.fit(X_train_vectorized, y_train)


# Evaluate model
predictions = model.predict(X_test_vectorized)

accuracy = accuracy_score(y_test, predictions)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, predictions))


# Create model directory
os.makedirs("model", exist_ok=True)


# Save model and vectorizer
joblib.dump(model, "model/model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")


print("\nModel saved successfully!")
print("Location: model/model.pkl")
print("Location: model/vectorizer.pkl")