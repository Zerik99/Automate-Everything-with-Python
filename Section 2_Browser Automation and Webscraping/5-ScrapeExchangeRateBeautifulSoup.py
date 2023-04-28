from bs4 import BeautifulSoup
import requests


def get_currency(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])
    return rate


def main():
    conversionRate = get_currency("Eur", "USD")
    return conversionRate


if __name__ == "__main__":
    print(main())
