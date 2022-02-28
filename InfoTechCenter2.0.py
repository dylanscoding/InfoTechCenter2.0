# Codename Hornet
# https://realpython.com/python-sleep/#adding-a-python-sleep-call-with-timesleep
# https://ozzmaker.com/add-colour-to-text-in-python/
import random

## Welcome Script

from time import sleep  # imports the sleep function from time
print("\033[1;32m This text is Bright Green  \n")
print("Welcome to Hornet's Info Tech Center!\n")
sleep(1)
print("\033[1;37;40m Hornet's Operating System Booting Up!")
sleep(1)

## Gas Script

# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty Tank", "Low Tank", "Quarter Tank", "Half Tank", "3 Quarters Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel
###

# Variable calls the value of gas Level Gauge Function
gasLevelIndicator = gasLevelGauge()

# Create If-Elif-Else statements using Comparative Operators(equalTo == equalTo) to display gas level messages
def gasLevelAlert():

    gasStations = ["Shell", "BP", "Citgo", "Circle K", "Mobil", "Speedway", "Marathon", "Love's", "Meijers", "Costco", "Sunoco"]
    print()
    if gasLevelIndicator == "Empty Tank":
        print("\033[1;31m  ***CRITICAL WARNING YOU ARE ON EMPTY***\nGas tank is empty. \nCalling emergency contact(s)")
    elif gasLevelIndicator == "Low Tank":
        print("\033[1;32m  ***NEARING CRITICAL WARNING***\nGas tank is LOW. \nCalculating closest gas station(s): " + random.choice(gasStations) + " that is " + str(random.randint(1, 50)) + " miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("\033[1;32m  ***WARNING***\nGas tank is only fueled for a QUARTER TANK. \nCalculating closest gas station(s): " + random.choice(gasStations) + " that is " + str(random.randint(1, 50)) + " miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("\033[1;32m  ***WARNING***\nGas tank is at HALF TANK. \n125 miles left!")
    elif gasLevelIndicator == "3 Quarters Tank":
        print("\033[1;32m  ***ALERT***\nGas tank is at THREE QUARTER TANK. \n320 miles left!")
    else:
        print("\033[1;32m  ***ALERT***\nGas tank is FULL. \nCongratulations, you have 560 miles left!")
###

# Calls the Alert function
gasLevelAlert()

## Weather Branch

def weather():
    weatherForecast = ["Icy", "Snowy", "Raining", "Windy", "Foggy", "Sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "Icy":
        print("\nVRS has changed your alarm 30 minutes earlier based on the NWS forecast of ", weatherAlert, ":(")
        print("\nVRS will only allow your car to go 30MPH")
    elif weatherAlert == "Snowy":
        print("\nVRS has changed your alarm 15 minutes earlier based on the NWS forecast of ", weatherAlert, ":(")
        print("\nVRS will only allow your car to go 50MPH")
    elif weatherAlert == "Raining":
        print("\nVRS has changed your alarm 5 minutes earlier based on the NWS forecast of ", weatherAlert, ":(")
        print("\nVRS will only allow your car to go 60MPH")
    elif weatherAlert == "Windy":
        print("\nVRS has changed your alarm 5 minutes earlier based on the NWS forecast of ", weatherAlert, ":(")
        print("\nVRS will only allow your car to go 70MPH")
    elif weatherAlert == "Foggy":
        print("\nVRS has changed your alarm 5 minutes earlier based on the NWS forecast of ", weatherAlert, ":(")
        print("\nVRS will only allow your car to go 60MPH")
    else:
        print("\nIt's sunny out! YAY!!!")
        print("\nVRS will only allow your car to go 120MPH")

vehicleResponseSystem()