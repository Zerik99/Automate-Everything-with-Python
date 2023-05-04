import os
import yagmail
from selenium import webdriver
import SeleniumWebDriverClass as swdc
from time import sleep

"""The stock price notifier app is a Python application that 
- get stock price data
- send a notification: when the price of a stock falls below a certain threshold. 

The app uses zse.hr to get the stock price data."""


def main(url) -> None:
    # create a webdriver object
    driver = create_webdriver(url=url)

    # get stock price change percent
    stockPriceChange = get_stock_price_change_percent(driver=driver)

    # send notification if stock price change is less than -0.10%
    if stockPriceChange > -0.05:
        print("No Notification Sent!")
    Status = send_email_notification(stockPriceChange)
    print(Status)


def create_webdriver(url) -> webdriver.Chrome:
    myWebDriver = swdc.WebDriverTemplate(siteURL=url)
    driver = myWebDriver.get_driver()
    return driver


def get_stock_price_change_percent(driver: webdriver.Chrome) -> float:
    xpath = "/html/body/div[2]/div/section[1]/div/div/div[2]/span[2]"
    stockPriceChangePercent = driver.find_element(by="xpath", value=xpath).text
    driver.quit()

    print(stockPriceChangePercent)
    return float(stockPriceChangePercent.replace("%", ""))


def send_email_notification(spChange: float) -> str:
    sender = os.environ.get("Py_Automation_Gmail")
    senderpw = os.environ.get("Py_Automation_Gmail_App_Pw")
    receiver = os.environ.get("Personal_Gmail")

    subject = "Stock Price Change alert!"

    contents = f"""\
    The Stock price is down {spChange}%. """

    yag = yagmail.SMTP(sender, senderpw)
    try:
        yag.send(to=receiver, subject=subject, contents=contents)
    except Exception as e:
        status = f"Email not sent! Error type: {type(e)} "
        return status
    else:
        status = "Email sent successfully!"
        return status


if __name__ == "__main__":
    _url = "https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6"
    main(_url)
