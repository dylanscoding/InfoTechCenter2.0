import random

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
    if gasLevelIndicator == "Empty Tank":
        print("\033[1;31m  ***CRITICAL WARNING YOU ARE ON EMPTY***\nGas tank is empty. \nCalling emergency contact(s)")
    elif gasLevelIndicator == "Low Tank":
        print("\033[1;32m  ***NEARING CRITICAL WARNING***\nGas tank is LOW. \nCalculating closest gas station(s)")
    elif gasLevelIndicator == "Quarter Tank":
        print("\033[1;32m  ***WARNING***\nGas tank is only fueled for a QUARTER TANK. \nCalculating closest gas station(s)")
    elif gasLevelIndicator == "Half Tank":
        print("\033[1;32m  ***WARNING***\nGas tank is at HALF TANK. \n125 miles left!")
    elif gasLevelIndicator == "3 Quarters Tank":
        print("\033[1;32m  ***ALERT***\nGas tank is at THREE QUARTER TANK. \n320 miles left!")
    else:
        print("\033[1;32m  ***ALERT***\nGas tank is FULL. \nCongratulations, you have 560 miles left!")
###

# Calls the Alert function
gasLevelAlert()
