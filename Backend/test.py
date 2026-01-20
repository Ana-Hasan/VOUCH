from preprocess import preprocess
from features import extract_features

sample = "this PRODUCT is Amazing!!!!!"
print(preprocess(sample))

review = "wow this was a fantastic and delightful experience and stay fabulous"
print(extract_features(preprocess(review)))