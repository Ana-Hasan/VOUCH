import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "..", "Database")
os.makedirs(DB_DIR, exist_ok=True)

DB_PATH = os.path.join(DB_DIR, "reviews.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            review_text TEXT,
            score REAL,
            label TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_review(review_text, score, label):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO reviews (review_text, score, label) VALUES (?, ?, ?)",
        (review_text, score, label)
    )

    conn.commit()
    conn.close()


def get_all_reviews():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT review_text, score, label FROM reviews ORDER BY id DESC"
    )

    rows = cursor.fetchall()
    conn.close()
    return rows


def clear_reviews():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM reviews")

    conn.commit()
    conn.close()
