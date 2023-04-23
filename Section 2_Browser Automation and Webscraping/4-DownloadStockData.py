import requests
from datetime import datetime as dt
import time
"""A script that downloads stock data from yahoo finance."""

"""The point of the section is to understand that using the GUI isn't always the best way to do things.
    Sometimes it's better to use the API's that are available to us."""

"""Browser automation and webscraping are two different things.
    Browser automation is when you use a script to automate a browser by manipulating the user interface.
    Webscraping is when you use a script to scrape data from a website via APIs or the URL."""

"""selenium functions as a hybrid between browser automation and webscraping."""


def convert_date_to_epoch():
    """converts date to epoch time"""
    from_date_input = input('Enter the start date in the format YYYY/MM/DD: ')
    to_date_input = input('Enter the end date in the format YYYY/MM/DD: ')

    # convert to date time object
    from_date = dt.strptime(from_date_input, '%Y/%m/%d')
    to_date = dt.strptime(to_date_input, '%Y/%m/%d')

    # Convert to epoch time
    convertedfrom_date = int(time.mktime(from_date.timetuple()))
    convertedto_date = int(time.mktime(to_date.timetuple()))
    return convertedfrom_date, convertedto_date


def main():
    """using requests download finance data from yahoo finance and create a csv file"""
    tickerSymbol = input('Enter the ticker symbol: ')
    interval = "1d"
    period_start, period_end = convert_date_to_epoch()

   # open url to download data with variables.
    URL = f"https://query1.finance.yahoo.com/v7/finance/download/{tickerSymbol}?period1={period_start}&period2={period_end}&interval={interval}&events=history&includeAdjustedClose=true"

    # the headers masks the fact that we are using a script to download the data.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}
    content = requests.get(URL, headers=headers).content

    with open(f"{tickerSymbol}-historicaldata.csv", "wb") as f:
        f.write(content)


if (__name__ == "__main__"):
    print(main())
