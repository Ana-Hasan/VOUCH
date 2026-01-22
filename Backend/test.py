from preprocess import preprocess
from features import extract_features
from detector import detector_function
from db import create_table, insert_review

review = "This product is amazing amazing best ever"

words = preprocess(review)
features = extract_features(words)
score, label = detector_function(features)

create_table()
insert_review(review, score, label)

print("Review:", review)
print("Features:", features)
print("Score:", score)
print("Label:", label)

import sqlite3

conn = sqlite3.connect("database/reviews.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM reviews")
rows = cursor.fetchall()

print("\nDatabase rows:")
for row in rows:
    print(row)

conn.close()

