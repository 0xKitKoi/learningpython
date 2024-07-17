import pandas as pd
import requests
from bs4 import BeautifulSoup


def main2():
    page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.13859000000008&lon=-117.29191999999995')
    soup = BeautifulSoup(page.content, 'html.parser')
    week = soup.find(id='seven-day-forecast-body')
    # print(week)

    items = week.find_all(class_= 'tombstone-container')
    #print(items[0])
    #  scrapes the data from each class from the website.
    # print(items[0].find(class_='period-name').get_text())
    # print(items[0].find(class_='short-desc').get_text())
    # print(items[0].find(class_='temp').get_text())

    period_names = [item.find(class_='period-name').get_text() for item in items]
    short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
    temperature = [item.find(class_='temp').get_text() for item in items]
    # print(period_names)
    # print(short_descriptions)
    # print(temperature)

    # Write scraped data into a csv file.
    # Create Dictionary
    weather_stuff = pd.DataFrame(
        {'period': period_names,
        'short_descriptions': short_descriptions,
        'temp': temperature
        })
    print(weather_stuff)
    # weather_stuff.to_csv('weather.csv')
