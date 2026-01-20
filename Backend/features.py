import numpy as np
positive_words = {
    "wow", "amazing", "fantastic", "great", "love", "excellent", "happy", "joy", "wonderful", "pleased", "delighted",
    "satisfied", "thrilled", "brilliant", "outstanding", "superb", "fabulous", "incredible", "marvelous", "spectacular",
    "exceptional", "phenomenal", "remarkable", "terrific", "awesome", "impressive", "magnificent", "splendid", "glorious",
    "radiant", "cheerful", "jubilant", "elated", "content", "upbeat", "optimistic", "enthusiastic", "euphoric",
}
def extract_features(words):
    total_words = len(words)
    if total_words == 0:
        return np.array([0.0])  
    positive_count = sum(1 for word in words if word in positive_words)
    positive_ratio = positive_count / total_words
    return np.array([total_words, positive_ratio])