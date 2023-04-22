# scrape simple text from a website.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


def get_driver():
    # here we are setting options for the webdriver. This makes automation easier with Selenium.
    wdoptions = webdriver.ChromeOptions()
    wdoptions.add_argument("disable-infobars",)
    wdoptions.add_argument("start-maximized")
    wdoptions.add_argument("disable-dev-shm-usage")
    wdoptions.add_argument("no-sandbox")
    wdoptions.add_experimental_option("excludeSwitches", ["enable-automation"])
    wdoptions.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(service=Service(
        "C:\Program Files (x86)\chromedriver.exe"), options=wdoptions)

    driver.get("http://automated.pythonanywhere.com")
    return driver


def main():
    driver = get_driver()
    elementByXpath = driver.find_element(
        by="xpath", value="/html/body/div[1]/div/h1[1]")
    return elementByXpath.text


print(main())
