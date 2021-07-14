import requests
import json


def get_weather_data(api_key):
    """Gets weather data from OpenWeatherMap

    Parameters
    ----------
    api_key : str
        The API key used to make requests to the OpenWeatherMap API.

    Returns
    -------
    dict
        Weather data for the specified location.
    """

    # Construct a URL with the specified parameters
    url = "https://api.openweathermap.org/data/2.5/onecall"
    url = url + "?lat=44.950433005684886&lon=-122.99038677842634"
    url = url + "&exclude=current,minutely&appid="
    url = url + api_key
    url = url + "&units=imperial"

    # Receives a JSON serialized response from OpenWeatherMap API
    r = requests.get(url)

    # Deserializes JSON response into dictionary format
    data = json.loads(r.text)
    return data
