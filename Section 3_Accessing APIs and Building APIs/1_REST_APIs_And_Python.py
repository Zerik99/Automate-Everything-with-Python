import requests
from datetime import datetime
from datetime import timedelta

today = datetime.today()
past = today - timedelta(days=14)
topic = "United States"

key = open(
    "C:\\Users\\Erik\\Desktop\\Automate Everything with Python Course\\Section 3_Accessing APIs and Building APIs\\NewsAPI_APIKey.txt",
    "r",
).read()

r = requests.get(
    f"https://newsapi.org/v2/everything?qInTitle={topic.replace(' ', '%20')}&from={past}&to={today}&sortBy=popularity&language=en&apiKey={key}"
)
content = r.json()

print(content["articles"][0]["title"])
