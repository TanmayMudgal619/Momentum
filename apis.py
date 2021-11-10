import requests
import json


class Quote:
    def __init__(self, data):
        self.author = data["author"]
        self.quote = data["content"]


class Temp:
    def __init__(self, data):
        self.mtemp = round(int(data["main"]["temp"]) - 273.15, 4)
        self.weather = data["weather"]


def getQuote():
    response = requests.get("http://api.quotable.io/random")
    data = json.loads(response.text)
    return Quote(data)


def getTemp(lat, lon):
    response = requests.get("https://api.openweathermap.org/data/2.5/weather", {
        "lat": lat,
        "lon": lon,
        "appid": "8bef185f3776480af1768e81a9fb60a7"})
    data = json.loads(response.text)
    return Temp(data)


def getBG():
    response = requests.get(
        "https://api.unsplash.com/photos/random/?client_id=IsEVO9042g2CjvCDADsKyLIDIf497pqxqbCEZku26h8")
    data = json.loads(response.text)
    return data["urls"]["small"]
