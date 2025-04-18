from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import download
download("vader_lexicon")

def analyze_sentiment(comments):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_counts = {"Positive": 0, "Neutral": 0, "Negative": 0}

    for comment in comments:
        score = analyzer.polarity_scores(comment)["compound"]
        if score >= 0.05:
            sentiment_counts["Positive"] += 1
        elif score <= -0.05:
            sentiment_counts["Negative"] += 1
        else:
            sentiment_counts["Neutral"] += 1

    sentiment_counts["Total Comments"] = len(comments)
    return sentiment_counts
