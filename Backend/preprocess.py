import string
def preprocess(text):
    text = text.lower()
    for char in string.punctuation:
        text = text.replace(char, " ")
        words = text.split()
        return words