from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# A class to create a webdriver object.


class WebDriverTemplate:
    def __init__(self, siteURL):
        self.driver = ""
        self.service = ""
        self.wdoptions = ""
        self.driverPath = "C:/Program Files (x86)/chromedriver.exe"
        self.siteURL = siteURL

    # A method to add options to the webdriver.
    # This reduces the chance of errors occuring during the automation.
    # used in the get_driver method.
    def add_options(self):
        self.wdoptions = webdriver.ChromeOptions()
        self.wdoptions.add_argument("disable-infobars")
        self.wdoptions.add_argument("start-maximized")
        self.wdoptions.add_argument("disable-dev-shm-usage")
        self.wdoptions.add_argument("no-sandbox")
        self.wdoptions.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.wdoptions.add_argument("disable-blink-features=AutomationControlled")
        return self.wdoptions

    # A method to add a service to the webdriver.
    #  used in the get_driver method.
    def add_service(self):
        self.service = Service(f"{self.driverPath}")
        return self.service

    # A method to get and return a webdriver object.
    def get_driver(self):
        self.driver = webdriver.Chrome(
            service=self.add_service(), options=self.add_options()
        )
        self.driver.get(self.siteURL)
        return self.driver
