#Import Libraries Here
import time
import sys
import random
from time import sleep
#Welcome Branch Starts Here
timeToSleep = 2.5

print("\nWelcome to InfoTech Center V1.0\n")
time.sleep(timeToSleep)

#Code to have the ellipsis add a dot every .5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("InfoTech Center System Booting" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r prints a carriage return first
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted!")

#Gasoline Branch Starts Here
print("\n*****************************************\n")
print("Gasoline Branch\n")

#Function that lists Gas Levels, randomly choosing one and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Function that lists Gas Station, randomly choosing one and returning its value
def listOfGasStations():
    gasStations = ["Shell","Speedway","Marathon","Circle K","Mobile","Costco","Meijer","7Eleven"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby

#Function will call the gasLevelGauge to determine our gas level and then find a close gas station
#by calling the liftOfGasStations function if we are on Low or Quarter Tank
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1, 50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(2.5)
        print("\n    ***Calling Triple AAA***")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is LOW, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationsLow,"miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a QUARTER TANK, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationsQuarterTank,"miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is on a HALF TANK which is plenty to get to your destination")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is on a THREE QUARTER TANK which is plenty to get to your destination")
    else:
        print("Your gas tank is FULL, HORRAYYYYYYY VROOOM VROOOM!!")

gasLevelAlert()


print("\n*****************************************\n")

print("Weather Branch")


#Create a function that randomly chooses the weather from a list
def weather():
    weatherForecast = ["Snowing", "Blizzard", "Raining", "Foggy", "Windy", "Icy", "Sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

#Variable to call the weather() once VRS(Vehicle Response System) is determined
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "Snowing":
        print("\nNational Weather Service has updated our alarm by 30 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 50mph.")
    elif weatherAlert == "Blizzard":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 40mph.")
    elif weatherAlert == "Raining":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 60mph.")
    elif weatherAlert == "Foggy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 60mph.")
    elif weatherAlert == "Windy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 70mph.")
    elif weatherAlert == "Icy":
        print("\nNational Weather Service has updated our alarm by 60 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 30mph.")
    else:
        print("\nNational Weather Service forecasts", weatherAlert,"weather conditions.")
        sleep(1.5)
        print("VRS has been disengaged! Drive at your own risk.")


vehicleResponseSystem()

