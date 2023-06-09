import SeleniumWebDriverClass
from selenium.webdriver.common.keys import Keys
import time


def main():
    siteURL = "http://automated.pythonanywhere.com/login/"
    driver = SeleniumWebDriverClass.WebDriverTemplate(
        siteURL=siteURL).get_driver()
    driver.find_element(by="id", value="id_username").send_keys("automated")

    driver.find_element(by="id", value="id_password").send_keys(
        "automatedautomated" + Keys.ENTER)
    time.sleep(2)
    # click home in navbar.
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()


if (__name__ == "__main__"):
    print(main())
