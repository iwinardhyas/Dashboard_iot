import time
import requests
from pprint import pprint

settings = {
    'api_key':'',
    'city_name':'Jakarta',
    'country_code':'id',
    'temp_unit':'Celsius'} #unit can be metric, imperial, or kelvin

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q={0},{1}&APPID={2}&units={3}"

def data_openweather():
    final_url = BASE_URL.format(settings["city_name"],settings["country_code"],settings["api_key"],settings["temp_unit"])
    weather_data = requests.get(final_url).json()
    temperature = (weather_data["main"]["temp"]-273.15)
    humidity = (weather_data["main"]["humidity"])
    pressure = (weather_data["main"]["pressure"])
    weather = (weather_data["weather"][0]["main"])
    wind = (weather_data["wind"]["speed"])
    # pprint(weather_data)
    # print(temperature)
    # print(humidity)
    # print(pressure)
    # print(weather)
    # print(wind)

    # time.sleep(10) #get new data every 20 seconds
    return temperature,humidity,pressure, weather,wind

data_openweather()