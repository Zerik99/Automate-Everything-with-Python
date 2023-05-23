"""A Chatbot to answer questions using Wikipedia."""
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import wikipedia


def main() -> None:
    """Run main function."""
    while True:
        question: str = input("Ask me a question. \n")

        if question == "quit":
            break

        search_text: str = wikipedia.page("vegetable").content

        st_tokenized_sentence: list[str] = get_tokenized_sentence(search_text)
        st_tokenized_sentence.append(question)

        most_similar_sentence: str = get_most_similar_sentence(
            get_lemma_sentence, st_tokenized_sentence
        )
        print(f'Here is what I found \n "{most_similar_sentence}" \n')


def get_lemma_sentence(_sentence: str) -> list[str]:
    """Returns the lemmatized version of a sentence."""
    sentence_tokens: list[str] = nltk.word_tokenize(_sentence.lower())

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


def get_tokenized_sentence(_sentence: str) -> list[str]:
    """Returns the tokenized version of a sentence."""
    sentence_tokens: list[str] = nltk.sent_tokenize(_sentence.lower())
    return sentence_tokens


def get_most_similar_sentence(_tokenizer, _sentence_tokens) -> str:
    """Returns the similarity coefficient between two sentences."""
    vectorizer = TfidfVectorizer(tokenizer=_tokenizer)

    tf = vectorizer.fit_transform(_sentence_tokens)

    values = cosine_similarity(tf[-1], tf)

    index = values.argsort()[0][-2]

    coeff = values.flatten().argsort()[-2]

    if coeff > 0.6:
        return _sentence_tokens[index]
    else:
        return "Sorry, I couldn't find any relevant info."


if __name__ == "__main__":
    main()
