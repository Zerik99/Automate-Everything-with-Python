import os
import yagmail
import SeleniumWebDriverClass as swdc
from time import sleep

"""The stock price notifier app is a Python application that 
- get stock price data
- send a notification: when the price of a stock falls below a certain threshold. 

The app uses zse.hr to get the stock price data."""


def main(stockPriceChange: float = 0.0, notifyCoolDown: int = 0) -> None:
    while True:
        # get stock price change percent
        try:
            stockPriceChange = get_stock_price_change_percent()
        except Exception as e:
            print(type(e))
            sleep(5)
            continue

        # send notification if stock price change is less than -0.10%
        if stockPriceChange > -0.05 or notifyCoolDown > 0:
            print("No Notification Sent! requirements not met.")
            notifyCoolDown -= 1
            sleep(5)
            continue
        send_email_notification(stockPriceChange)
        notifyCoolDown = 2
        sleep(5)


def get_stock_price_change_percent() -> float:
    url = "https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6"
    xpath = "/html/body/div[2]/div/section[1]/div/div/div[2]/span[2]"

    myWebDriver = swdc.WebDriverTemplate(siteURL=url)
    driver = myWebDriver.get_driver()
    sleep(3)

    stockPriceChangePercent = driver.find_element(by="xpath", value=xpath).text
    driver.quit()

    print(stockPriceChangePercent)
    return float(stockPriceChangePercent.replace("%", ""))


def send_email_notification(spChange: float) -> None:
    sender = os.environ.get("Py_Automation_Gmail")
    senderpw = os.environ.get("Py_Automation_Gmail_App_Pw")
    receiver = os.environ.get("Personal_Gmail")

    subject = "Stock Price Change alert!"

    contents = f"""\
    The Stock price is down {spChange}%. """

    yag = yagmail.SMTP(sender, senderpw)
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")


if __name__ == "__main__":
    main()
