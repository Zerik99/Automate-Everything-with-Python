import requests
from datetime import datetime, timedelta


def get_News(country: str, key: str) -> list:
    r = requests.get(
        f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={key}"
    )

    content = r.json()
    articles = content["articles"]

    for article in articles:
        print(
            f"Title:\n {article['title']}\n\n Description:\n {article['description']}\n\n"
        )

    return articles


if __name__ == "__main__":
    key = open(
        "C:\\Users\\Erik\\Desktop\\Automate Everything with Python Course\\Section 3_Accessing APIs and Building APIs\\NewsAPI_APIKey.txt",
        "r",
    ).read()
    #  "us" is a valid input.
    country = input("Press enter a country: ")

    articlesOUT = get_News(country=country, key=key)

    if len(articlesOUT) == 0:
        print("No articles found")
    else:
        print(f"Found {len(articlesOUT)} articles from {country}.")
