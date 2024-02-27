print("\n***********************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

#Create a function that randomly chooses the weather from a list
def weather():
    weatherForecast = ["Snowing", "Blizzard", "Raining", "Foggy", "Windy", "Icy", "Sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions


print(weather())