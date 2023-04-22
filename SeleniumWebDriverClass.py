from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# A class to create a webdriver object.


class WebDriverTemplate():
    def __init__(self, driver, service, wdoptions):
        self.driver = driver
        self.service = service
        self.wdoptions = wdoptions
        self.driverPath = "C:\\Program Files (x86)\\chromedriver.exe"

    def add_options(self):
        self.wdoptions = webdriver.ChromeOptions()
        self.wdoptions.add_argument("disable-infobars")
        self.wdoptions.add_argument("start-maximized")
        self.wdoptions.add_argument("disable-dev-shm-usage")
        self.wdoptions.add_argument("no-sandbox")
        self.wdoptions.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        self.wdoptions.add_argument(
            "disable-blink-features=AutomationControlled")
        return self.wdoptions

    def add_service(self):
        self.service = Service(f"{self.driverPath}")
        return self.service

    def get_driver(self):
        self.driver = webdriver.Chrome(service=self.add_service(
            driverPath=self.driverPath), options=self.wdoptions)
        return self.driver
