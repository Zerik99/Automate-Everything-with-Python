import SeleniumWebDriverClass
import time


def clean_text(text):
    """remove all text from the average world temp text."""
    output = float(text.split(": ")[1])
    return output


def main():
    siteURL = "http://automated.pythonanywhere.com"
    driver = SeleniumWebDriverClass.WebDriverTemplate(
        siteURL=siteURL).get_driver()

    time.sleep(2)

    element = driver.find_element(
        by="xpath", value="/html/body/div[1]/div/h1[2]")

    return clean_text(element.text)


if (__name__ == "__main__"):
    print(main())
