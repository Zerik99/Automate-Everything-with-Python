import SeleniumWebDriverClass
import time
import datetime
from selenium.webdriver.common.keys import Keys
"""A script that scrapes the average world temperature and writes to a text file."""


def clean_text(text):
    """Extract the average world temperature from the text and store in a txt file."""
    output = float(text.split(": ")[1])
    return output


def write_to_file(text):
    filename = f"{datetime.date.today().strftime('%Y-%m-%d')}.txt"
    """Write the average world temperature to a txt file."""
    with open(filename, "a") as file:
        file.write(text)
        print(f"Writing {text}to {filename}")


def main():
    """Main function that calls the other functions."""
    counter = 0
    siteURL = "http://automated.pythonanywhere.com"
    # instantiate driver
    driver = SeleniumWebDriverClass.WebDriverTemplate(
        siteURL=siteURL).get_driver()

    # run a loop that scrapes the average world temp every 2 seconds.
    while (counter < 10):
        counter += 1
        # Wait 2 second then scrape average world temp.
        time.sleep(2)
        average_world_temp = driver.find_element(
            by="xpath", value="/html/body/div[1]/div/h1[2]")
        write_to_file(str(clean_text(average_world_temp.text)) + " ")
    return


if (__name__ == "__main__"):
    print(main())
