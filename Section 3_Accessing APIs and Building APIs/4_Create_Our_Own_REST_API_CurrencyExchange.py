from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests


def get_currency(in_curr, out_curr):
    url = f"https://www.x-rates.com/calculator/?from={in_curr}&to={out_curr}&amount=1"
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])
    return rate


app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Currency rate API</h1> <p>Use the following URL to get the currency rate: /api/v1/usd-eur</p>"


@app.route("/api/v1/<in_curr>-<out_curr>")
def api(in_curr, out_curr):
    rate = get_currency(in_curr, out_curr)
    result_dictionary = {
        "input_currency": in_curr,
        "output_currency": out_curr,
        "rate": rate,
    }
    return jsonify(result_dictionary)


app.run()
