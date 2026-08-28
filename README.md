# 📰 Fake News Detector

A modern Machine Learning-based Fake News Detection System developed using Python, Flask, Scikit-learn, Natural Language Processing (NLP), and SQLite. The application helps users analyze news content and predict whether it is likely **REAL** or **FAKE**.

The system uses TF-IDF vectorization and a Logistic Regression model to process textual news content, calculate prediction confidence, maintain prediction history, and provide dashboard analytics.

---

## 🌐 Live Demo

**Live Website:**  
https://fake-news-detector-0ims.onrender.com/

**GitHub Repository:**  
https://github.com/sanjanard11/Fake-News-Detector

---

# 📌 About This Project

### Machine Learning and Web Development Project

The Fake News Detector is designed to simplify the process of analyzing news articles and statements using Machine Learning and Natural Language Processing.

The application enables users to:

* Analyze news articles and statements
* Predict whether content is REAL or FAKE
* View prediction confidence
* Track previous predictions
* Monitor dashboard statistics
* Delete individual prediction records
* Clear prediction history
* Understand the AI analysis workflow

### 📦 Deliverable

A live Machine Learning web application with source code hosted on GitHub.

**Developer:** SANJANA RD  
**Project Type:** Machine Learning and Web Application

---

# 🎯 Project Objectives

* Detect potentially fake news content
* Apply Machine Learning for text classification
* Use NLP for text processing
* Provide prediction confidence
* Maintain prediction history
* Provide dashboard analytics
* Create a user-friendly interface
* Develop a responsive and modern web application

---

# ✨ Features

## 🎨 Frontend Features

* Modern Responsive UI
* AI-Powered News Analysis Interface
* News Content Input Panel
* Prediction Result Dashboard
* Confidence Progress Bar
* Dashboard Statistics
* Prediction History
* Delete Prediction Option
* Clear History Option
* Responsive Design
* User-Friendly Interface

## 🔧 Backend Features

* Flask Web Server
* Machine Learning Model Integration
* SQLite Database Integration
* Prediction History Management
* Confidence Calculation
* Error Handling
* Model Loading Using Joblib

---

# 📋 Core Functionalities

## 📰 News Analysis

* Enter News Content
* Analyze News Articles
* Analyze News Statements
* Process Text Using NLP
* Generate Machine Learning Predictions

## 🤖 Fake News Prediction

* Predict REAL News
* Predict FAKE News
* Calculate Prediction Confidence
* Display Confidence Level
* Provide AI Analysis Insights

## 📊 Dashboard Analytics

* Total Predictions Count
* Reliable News Overview
* Potentially Fake News Overview
* Average Confidence Score
* Prediction Activity Monitoring

## 📜 Prediction History

* Store Previous Predictions
* View Recent Predictions
* Display Prediction Result
* Display Confidence Percentage
* Display Confidence Level
* Display Prediction Date and Time
* Delete Individual Predictions
* Clear Complete History

---

# 🛠 Technologies Used

## Frontend

* HTML5
* CSS3
* Jinja2 Templates

## Backend

* Python
* Flask

## Machine Learning

* Scikit-learn
* Logistic Regression
* TF-IDF Vectorizer
* Natural Language Processing (NLP)

## Database

* SQLite

## Data Processing

* Pandas
* NumPy

## Additional Packages

* Joblib
* Gunicorn

---

# 🧠 Machine Learning Workflow

```text
News Input
    ↓
Text Processing
    ↓
TF-IDF Vectorization
    ↓
Logistic Regression Model
    ↓
Prediction
    ↓
Confidence Calculation
    ↓
Store Result in SQLite Database

Fake-News-Detector/
│
├── app.py
├── train_model.py
├── requirements.txt
├── Procfile
├── database.db
├── README.md
├── LICENSE
│
├── dataset/
│   └── news.csv
│
├── model/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── static/
│   └── style.css
│
└── templates/
    └── index.html

🌐 Deployment

The application is deployed using:

Render
Gunicorn

⚠️ Disclaimer

This application provides a Machine Learning-based prediction and should not be considered a definitive fact-checking service.

The predictions are generated based on patterns learned from the training dataset. Users should always verify important information using trusted and reliable sources.

📄 License

This project is licensed under the MIT License.

👩‍💻 Developer

**SANJANA RD**

Computer Science Engineering Student

GitHub:
https://github.com/sanjanard11

⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Happy Coding! 🚀
