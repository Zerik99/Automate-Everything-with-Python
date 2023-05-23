"""a simple app to demonstrate finding the lemma of words. Will use NLTK."""
from nltk.stem import WordNetLemmatizer

x = "was"
y = "is"

word_lemmatizer = WordNetLemmatizer()

lemma = word_lemmatizer.lemmatize(x, pos="v")
lemma2 = word_lemmatizer.lemmatize(y, pos="v")

print(lemma)
print(lemma2)
