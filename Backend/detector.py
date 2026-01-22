import numpy as np

def detector_function(features):
    total_words = features[0]
    positive_ratio = features[1]

    score = 0

    if total_words < 5:
        score += 0.4

    if positive_ratio >= 0.5:
        score += 0.6

    if score >= 0.4:
        label = "Fake review"
    else:
        label = "Genuine review"

    return score, label
