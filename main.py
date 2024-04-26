from textblob import TextBlob

text = "I love this product! It's amazing."

blob = TextBlob(text)

sentiment = blob.sentiment
if __name__ == "__main__":
    print("Text:", text)
    print("Polarity:", sentiment.polarity)
    print("Subjectivity:", sentiment.subjectivity)
