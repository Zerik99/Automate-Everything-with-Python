"""A simple app to demonstrate lemmatisation of sentences. Will use NLTK."""
import nltk

from nltk.stem import WordNetLemmatizer

sentence = "Vegetables are types of plants."

sentence_tokens: list[str] = nltk.word_tokenize(sentence.lower())
# print(sentence_tokens)
pos_tags = nltk.pos_tag(sentence_tokens)
# print(pos_tags)
lemmatizer = WordNetLemmatizer()

# using list comprehension:
lemma_sentence: list[str] = [
    lemmatizer.lemmatize(
        word=token, pos=pos_tag[1][0].lower()
    )  # get lemmatization of word
    for token, pos_tag in zip(sentence_tokens, pos_tags)  # for each word in sentence
    if pos_tag[1][0].lower()
    in ["n", "v", "a", "r"]  # if the word is a noun, verb, adjective or adverb
]

print(lemma_sentence)


# Not using list comprehension:
# for token, pos_tag in zip(sentence_tokens, pos_tags):
#     if pos_tag[1][0].lower() not in ["n", "v", "a", "r"]:
#         print(
#             token
#         )  # not needed for natural language processing, could be used for debugging
#         continue
#     lemma = lemmatizer.lemmatize(word=token, pos=pos_tag[1][0].lower())
#     print(lemma)
