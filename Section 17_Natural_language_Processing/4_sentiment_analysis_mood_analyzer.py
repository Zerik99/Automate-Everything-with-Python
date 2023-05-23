"""a simple app to demonstrate sentiment analysis using NLTK."""
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

# text1 = "Great job!"
# sentiment = analyzer.polarity_scores(text1)

twitter_samples = nltk.corpus.twitter_samples.strings()

twitter_sentiment: dict[str, list[int]] = {"pos": [0], "neg": [0], "neu": [0]}

# for each tweet in twitter_samples increase counter for positive, negative or neutral sentiment.
for tweet in twitter_samples:
    sentiment: dict[str, float] = analyzer.polarity_scores(tweet)
    if sentiment["compound"] > 0:
        twitter_sentiment["pos"][0] += 1
        print("Positive")
    elif sentiment["compound"] < 0:
        twitter_sentiment["neg"][0] += 1
        print("Negative")
    else:
        twitter_sentiment["neu"][0] += 1
        print("Neutral")

print(twitter_sentiment)
