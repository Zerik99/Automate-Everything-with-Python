import requests
from datetime import datetime, timedelta


def get_News(topic: str, past: datetime, today: datetime, key: str) -> list:
    r = requests.get(
        f"https://newsapi.org/v2/everything?qInTitle={topic.replace(' ', '%20')}&from={past}&to={today}&sortBy=popularity&language=en&apiKey={key}"
    )

    content = r.json()
    articles = content["articles"]

    for article in articles:
        print(
            f"Title:\n {article['title']}\n\n Description:\n {article['description']}\n\n"
        )

    return articles


if __name__ == "__main__":
    today = datetime.today()
    past = today - timedelta(days=14)
    key = open(
        "C:\\Users\\Erik\\Desktop\\Automate Everything with Python Course\\Section 3_Accessing APIs and Building APIs\\NewsAPI_APIKey.txt",
        "r",
    ).read()
    topic = input("Press enter a topic to search for: ")

    articlesOUT = get_News(topic=topic, today=today, past=past, key=key)

    if len(articlesOUT) == 0:
        print("No articles found")
    else:
        print(f"Found {len(articlesOUT)} articles on your topic '{topic}'.")
