"""This exercise is to use the openweathermap API to get Weather data for a city of your choice.

Expected output: Append data to a file called weather_data.txt
It should contain the following information:
city, Time, Temperature, and Condition."""

import requests
from datetime import datetime
from dataclasses import dataclass


# Since we are working with data it may be appropriate to use a dataclass.
@dataclass
class WeatherData:
    city: str
    time: datetime
    temperature: float
    condition: str


def get_key() -> str:
    key = open(
        "C:\\Users\\Erik\\Desktop\\Automate Everything with Python Course\\Section 3_Accessing APIs and Building APIs\\OpenWeatherAPI_APIKey.txt",
        "r",
    ).read()
    return key


def get_weather(city: str, key: str) -> list:
    r = requests.get(
        f"https://api.openweathermap.org/data/2.5/forecast?units=imperial&q={city}&appid={key}"
    )

    content = r.json()
    days = content["list"]
    WeatherDataList = []

    for day in days:
        weatherdata = WeatherData(
            city=city,
            time=datetime.fromtimestamp(day["dt"]),
            temperature=day["main"]["temp"],
            condition=day["weather"][0]["description"],
        )
        WeatherDataList.append(weatherdata)
    return WeatherDataList


def main():
    key = get_key()
    city = input("Enter a city: ")
    weatherforecastlist = get_weather(city=city, key=key)

    with open(
        "Section 3_Accessing APIs and Building APIs\\weather_data.txt", "a"
    ) as file:
        for weatherdata in weatherforecastlist:
            file.write(
                f"{weatherdata.city}, {weatherdata.time}, {weatherdata.temperature}, {weatherdata.condition}\n"
            )


if __name__ == "__main__":
    main()
