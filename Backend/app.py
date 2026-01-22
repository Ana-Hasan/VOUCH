from flask import Flask, request, jsonify
from preprocess import preprocess
from features import extract_features
from detector import detector_function
from db import create_table, insert_review
from flask import render_template
from db import create_table, insert_review, get_all_reviews, clear_reviews



app = Flask(__name__)

create_table()
@app.route("/clear", methods=["POST"])
def clear_history():
    clear_reviews()
    return jsonify({"status": "cleared"})

@app.route("/history", methods=["GET"])
def history():
    rows = get_all_reviews()

    reviews = []
    for r in rows:
        reviews.append({
            "text": r[0],
            "score": r[1],
            "label": r[2]
        })

    return jsonify(reviews)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    review = data.get("review", "")

    words = preprocess(review)
    features = extract_features(words)
    score, label = detector_function(features)

    insert_review(review, score, label)

    return jsonify({
        "score": score,
        "label": label
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

