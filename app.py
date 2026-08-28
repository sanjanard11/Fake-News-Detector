from flask import Flask, render_template, request, redirect, url_for
import joblib
import os
import sqlite3
from datetime import datetime

app = Flask(__name__)


# ==============================
# PATHS
# ==============================

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "model", "vectorizer.pkl")
DATABASE_PATH = os.path.join(BASE_DIR, "database.db")


# ==============================
# LOAD MODEL
# ==============================

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


# ==============================
# DATABASE FUNCTIONS
# ==============================

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS prediction_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            news_text TEXT NOT NULL,
            prediction TEXT NOT NULL,
            confidence REAL NOT NULL,
            confidence_level TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# Create database and table
initialize_database()


# ==============================
# HOME ROUTE
# ==============================

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    confidence = None
    confidence_level = None
    news_text = ""
    error = None

    # ==============================
    # ANALYZE NEWS
    # ==============================

    if request.method == "POST":

        news_text = request.form.get("news_text", "").strip()

        if len(news_text) < 20:

            error = "Please enter at least 20 characters for better analysis."

        else:

            try:

                # Convert text into TF-IDF features
                text_vector = vectorizer.transform([news_text])

                # Make prediction
                prediction = model.predict(text_vector)[0]

                # Calculate confidence
                probabilities = model.predict_proba(text_vector)[0]
                confidence = float(max(probabilities) * 100)

                # Determine confidence level
                if confidence >= 80:
                    confidence_level = "High"

                elif confidence >= 60:
                    confidence_level = "Moderate"

                else:
                    confidence_level = "Low"

                # Save prediction to database
                conn = get_db_connection()

                conn.execute(
                    """
                    INSERT INTO prediction_history
                    (
                        news_text,
                        prediction,
                        confidence,
                        confidence_level,
                        created_at
                    )
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        news_text,
                        prediction,
                        confidence,
                        confidence_level,
                        datetime.now().strftime("%d %b %Y, %I:%M %p")
                    )
                )

                conn.commit()
                conn.close()

            except Exception as e:
                error = str(e)

    # ==============================
    # GET HISTORY + STATISTICS
    # ==============================

    conn = get_db_connection()

    # Get latest 10 predictions
    history = conn.execute(
        """
        SELECT *
        FROM prediction_history
        ORDER BY id DESC
        LIMIT 10
        """
    ).fetchall()

    # Total predictions
    total_predictions = conn.execute(
        """
        SELECT COUNT(*)
        FROM prediction_history
        """
    ).fetchone()[0]

    # Total REAL predictions
    total_real = conn.execute(
        """
        SELECT COUNT(*)
        FROM prediction_history
        WHERE prediction = 'REAL'
        """
    ).fetchone()[0]

    # Total FAKE predictions
    total_fake = conn.execute(
        """
        SELECT COUNT(*)
        FROM prediction_history
        WHERE prediction = 'FAKE'
        """
    ).fetchone()[0]

    # Average confidence
    average_confidence = conn.execute(
        """
        SELECT AVG(confidence)
        FROM prediction_history
        """
    ).fetchone()[0]

    # Avoid None if database is empty
    if average_confidence is None:
        average_confidence = 0

    conn.close()

    # ==============================
    # RENDER PAGE
    # ==============================

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        confidence_level=confidence_level,
        news_text=news_text,
        error=error,
        history=history,
        total_predictions=total_predictions,
        total_real=total_real,
        total_fake=total_fake,
        average_confidence=average_confidence
    )


# ==============================
# DELETE ONE HISTORY ITEM
# ==============================

@app.route("/delete-history/<int:history_id>", methods=["POST"])
def delete_history(history_id):

    conn = get_db_connection()

    conn.execute(
        "DELETE FROM prediction_history WHERE id = ?",
        (history_id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("home"))


# ==============================
# CLEAR ALL HISTORY
# ==============================

@app.route("/clear-history", methods=["POST"])
def clear_history():

    conn = get_db_connection()

    conn.execute("DELETE FROM prediction_history")

    conn.commit()
    conn.close()

    return redirect(url_for("home"))


# ==============================
# RUN APPLICATION
# ==============================

if __name__ == "__main__":
    app.run(debug=True)