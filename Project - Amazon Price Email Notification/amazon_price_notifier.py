"""An App that notifies a user via email when the price of an item on Amazon drops below a certain price."""
from time import sleep
from SeleniumWebDriverClass import WebDriverTemplate as SeleniumWebDriver
import yagmail
import os


def main(_url) -> None:
    """The main function of the app."""
    my_webdriver = SeleniumWebDriver(_url)
    driver = my_webdriver.get_driver()
    sleep(3)
    xpath_whole_dollar = (
        '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]/span[2]/span[2]'
    )
    xpath_cents = (
        '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]/span[2]/span[3]'
    )

    dollar_str: str = driver.find_element("xpath", xpath_whole_dollar).text
    cents_str: str = driver.find_element("xpath", xpath_cents).text

    print(dollar_str + "\n")
    print(cents_str + "\n")

    send_email(clean_price(dollar_str, cents_str))


def clean_price(_dollar_str: str, _cents_str: str) -> float:
    """Cleans the price string and returns a float."""
    price_str = f"{_dollar_str}.{_cents_str}"
    price = float(price_str)
    return price


def send_email(_price):
    """Sends an email to the user with the price of the item and a link to the item."""
    sender = os.environ.get("Py_Automation_Gmail")
    senderpw = os.environ.get("Py_Automation_Gmail_App_Pw")
    receiver = os.environ.get("Personal_Gmail")

    subject = "Amazon Price Alert!"

    contents = f"""Your item is now below your desired price of ${_price}!"""

    yag = yagmail.SMTP(sender, senderpw)
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")


if __name__ == "__main__":
    URL = "https://www.amazon.com/PF-WaterWorks-PF0989-Disposal-Installation/dp/B078H38Q1M/"
    main(URL)
