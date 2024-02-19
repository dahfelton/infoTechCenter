print("*****************************************")
print("Gasoline Branch\n\n")

#Import Libraries Here
import random

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
    milesToGasStationsLow = random.uniform(1,25)
    milesToGasStationsQuarterTank = random.uniform(25.1, 50)
    gasLevelIndicator = gasLevelGauge()
    print(milesToGasStationsLow)
    print(milesToGasStationsQuarterTank)

gasLevelAlert()