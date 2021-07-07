import requests
import json


def get_weather_data(api_key):
    url = "https://api.openweathermap.org/data/2.5/onecall"
    url = url + "?lat=44.950433005684886&lon=-122.99038677842634"
    url = url + "&exclude=current,minutely&appid="
    url = url + api_key
    url = url + "&units=imperial"

    r = requests.get(url)
    data = json.loads(r.text)
    return data
