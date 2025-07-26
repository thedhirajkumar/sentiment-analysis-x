from flask import Flask, render_template, request
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt
import os

# Initialize NLTK VADER
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

# Load Sentiment140 dataset or use fallback
try:
    df = pd.read_csv("sentiment140.csv", encoding="ISO-8859-1", names=["target", "id", "date", "flag", "user", "text"])
    sample_texts = df["text"].head(10).tolist()
except FileNotFoundError:
    sample_texts = [
        "I love AI and coding! It's so fun!",
        "This is a terrible day, nothing works.",
        "Just another day."
    ]

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment_result = None

    if request.method == "POST":
        text = request.form["text"]
        scores = analyzer.polarity_scores(text)
        compound = scores["compound"]
        if compound >= 0.05:
            sentiment_result = "Positive"
        elif compound <= -0.05:
            sentiment_result = "Negative"
        else:
            sentiment_result = "Neutral"

    sentiments = []
    for text in sample_texts:
        scores = analyzer.polarity_scores(text)
        compound = scores["compound"]
        if compound >= 0.05:
            sentiments.append("Positive")
        elif compound <= -0.05:
            sentiments.append("Negative")
        else:
            sentiments.append("Neutral")

    sentiment_counts = pd.Series(sentiments).value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%")
    plt.title("Sentiment Distribution of Sample Tweets")
    plt.savefig("static/sentiment_plot.png")
    plt.close()

    return render_template("index.html", sentiment_result=sentiment_result, plot_url="static/sentiment_plot.png")

if __name__ == "__main__":
    app.run(debug=True)
