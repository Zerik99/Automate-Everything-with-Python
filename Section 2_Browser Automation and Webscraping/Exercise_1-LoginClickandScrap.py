import SeleniumWebDriverClass
import time
from selenium.webdriver.common.keys import Keys
"""A script that logs in, presses the home button, and scrapes the average world temperature."""


def clean_text(text):
    """Extract the average world temperature from the text."""
    output = float(text.split(": ")[1])
    return output


def main():
    siteURL = "http://automated.pythonanywhere.com/login/"
    driver = SeleniumWebDriverClass.WebDriverTemplate(
        siteURL=siteURL).get_driver()
    # login
    driver.find_element(by="id", value="id_username").send_keys("automated")
    driver.find_element(by="id", value="id_password").send_keys(
        "automatedautomated" + Keys.ENTER)
    # click home in navbar.
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    # scrape average world temp.
    time.sleep(2)
    average_world_temp = driver.find_element(
        by="xpath", value="/html/body/div[1]/div/h1[2]")
    return clean_text(average_world_temp.text)


if (__name__ == "__main__"):
    print(main())
