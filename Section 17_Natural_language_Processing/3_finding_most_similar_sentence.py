"""A simple app to demonstrate finding the most similar sentence using NLTK."""
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def main() -> None:
    """Run main function."""

    question = "What are vegetables?"
    search_text = "Originally, vegetables were collected from the wild by hunter-gatherers. Vegetables are all plants. Vegetables can be eaten either raw or cooked."

    q_lemma_sentence: list[str] = get_lemma_sentence(question)
    print(q_lemma_sentence)

    st_tokenized_sentence: list[str] = get_tokenized_sentence(search_text)
    st_tokenized_sentence.append(question)
    print(st_tokenized_sentence)

    # can probably turn this into a separate function

    vectorizer = TfidfVectorizer(tokenizer=get_lemma_sentence)

    tf = vectorizer.fit_transform(st_tokenized_sentence)

    values = cosine_similarity(tf[-1], tf)

    index = values.argsort()[0][-2]

    coeff = values.flatten().argsort()[-2]

    if coeff > 0.3:
        print(st_tokenized_sentence[index])


def get_lemma_sentence(sentence: str) -> list[str]:
    """Returns the lemmatized version of a sentence."""
    sentence_tokens: list[str] = nltk.word_tokenize(sentence.lower())

    pos_tags = nltk.pos_tag(sentence_tokens)

    lemmatizer = WordNetLemmatizer()

    lemma_sentence: list[str] = [
        lemmatizer.lemmatize(
            word=token, pos=pos_tag[1][0].lower()
        )  # get lemmatization of word
        for token, pos_tag in zip(
            sentence_tokens, pos_tags
        )  # for each word in sentence
        if pos_tag[1][0].lower()
        in ["n", "v", "a", "r"]  # if the word is a noun, verb, adjective or adverb
    ]
    return lemma_sentence


def get_tokenized_sentence(sentence: str) -> list[str]:
    """Returns the tokenized version of a sentence."""
    sentence_tokens: list[str] = nltk.sent_tokenize(sentence.lower())
    return sentence_tokens


if __name__ == "__main__":
    main()
