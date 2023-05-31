"""A simple script to test the speech_recognition library."""
import nltk
from speech_recognition import Recognizer, AudioFile
from nltk.sentiment import SentimentIntensityAnalyzer


recognizer = Recognizer()

with AudioFile("Project - Find the Mood of a Person/files/chile.wav") as source:
    audio = recognizer.record(source)

text = recognizer.recognize_google(audio)

analyzer = SentimentIntensityAnalyzer()

text_sentiment: dict[str, list[int]] = {"pos": [0], "neg": [0], "neu": [0]}

# for each tweet in twitter_samples increase counter for positive, negative or neutral sentiment.

sentiment: dict[str, float] = analyzer.polarity_scores(text)
if sentiment["compound"] > 0:
    text_sentiment["pos"][0] += 1
    print("Positive")
elif sentiment["compound"] < 0:
    text_sentiment["neg"][0] += 1
    print("Negative")
else:
    text_sentiment["neu"][0] += 1
    print("Neutral")

print(text_sentiment)
