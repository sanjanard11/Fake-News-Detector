# 📰 Fake News Detector

A professional **Machine Learning-based Fake News Detection web application** built using **Python, Flask, Natural Language Processing (NLP), and Scikit-learn**.

The application analyzes news articles or statements and predicts whether the content is likely **REAL** or **FAKE**. It also provides a confidence score, prediction history, dashboard analytics, and insights into the machine learning model.

---

## 🚀 Live Demo

🌐 **Live Application:**  
https://fake-news-detector-0ims.onrender.com

---

## ✨ Features

- 🤖 AI-powered news analysis
- 📰 Detects whether news content is **REAL** or **FAKE**
- 🎯 Displays prediction confidence percentage
- 🧠 Uses **Natural Language Processing (NLP)**
- 📊 Interactive dashboard statistics
- 📈 Tracks total predictions
- ✅ Shows reliable news predictions
- ⚠️ Shows potentially fake news predictions
- 🎯 Calculates average confidence
- 🕒 Stores recent prediction history
- 🗑️ Delete individual predictions
- 🧹 Clear complete prediction history
- 📄 Displays analyzed text length
- 💡 Provides AI analysis insights
- 🎨 Modern and responsive user interface

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- Jinja2 Templates

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Logistic Regression
- TF-IDF Vectorization
- Natural Language Processing (NLP)

### Data Processing
- Pandas
- NumPy

### Database
- SQLite

### Deployment
- Render
- Gunicorn

---

## 🧠 Machine Learning Workflow

The Fake News Detector follows these steps:

### 1️⃣ Enter News Content
The user enters or pastes a news article or statement into the application.

### 2️⃣ Text Processing
The news content is processed using Natural Language Processing techniques.

### 3️⃣ TF-IDF Vectorization
The text is converted into numerical features using **TF-IDF (Term Frequency–Inverse Document Frequency)**.

### 4️⃣ Machine Learning Prediction
A trained **Logistic Regression model** analyzes the processed text.

### 5️⃣ Result Generation
The system predicts whether the news is:

- ✅ **REAL**
- ⚠️ **FAKE**

### 6️⃣ Confidence Analysis
The application displays the confidence percentage of the prediction.

---

## 📊 Dashboard Analytics

The application provides a dashboard containing:

- 📊 Total Predictions
- ✅ Reliable News Count
- ⚠️ Potentially Fake News Count
- 🎯 Average Prediction Confidence

These statistics help users understand their overall news analysis activity.

---

## 📁 Project Structure

FakeNewsDetector/
│
├── app.py
├── train_model.py
├── requirements.txt
├── Procfile
├── database.db
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

🎯 Model Used

The application uses:

Logistic Regression

Logistic Regression is used as the classification algorithm to predict whether a news article is likely REAL or FAKE.

TF-IDF Vectorizer

TF-IDF converts textual news content into numerical features that can be processed by the machine learning model.


📸 Application Features

The web application includes:

Professional AI-powered landing interface
News content input section
AI model status indicator
Prediction result dashboard
Confidence progress bar
Model information
NLP processing details
Text length analysis
Prediction history
Dashboard statistics
Important fact-checking disclaimer


⚠️ Disclaimer

This application provides a machine-learning-based prediction and should not be considered a definitive fact-checking system.

Users should always verify important information using trusted and reliable sources.

🔮 Future Improvements
Integration with real-time news APIs
Advanced deep learning models
BERT-based text classification
User authentication system
Cloud database integration
News source credibility analysis
Visualization and analytics improvements
REST API support
Multi-language news analysis


👩‍💻 Author

**Sanjana RD**

**Computer Science Engineering Student**

**Skills** : 
Python
Machine Learning
HTML
CSS
Flask
NLP
Scikit-learn
SQL


⭐ Support

If you found this project useful, please consider giving the repository a star ⭐.
