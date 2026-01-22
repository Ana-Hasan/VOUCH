import sqlite3
import os

DB_PATH = os.path.join("Database", "reviews.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

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
