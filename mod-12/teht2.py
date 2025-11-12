import requests
import json
#22cf12c0b59921a8861f94d3661ef192
kaupunki = input("Syötä kaupungin nimi: ")
pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid=22cf12c0b59921a8861f94d3661ef192"

vastaus = requests.get(pyyntö).json()
print(f"The weather of your city is {vastaus['weather'][0]['description']}")
print(f"and the temperature is {int(vastaus['main']['temp']-273.15)}°C")