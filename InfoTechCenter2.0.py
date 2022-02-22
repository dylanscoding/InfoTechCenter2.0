import random
# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty Tank", "Low Tank", "Quarter Tank", "Half Tank", "3 Quarters Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Create If-Elif-Else statements using Comparative Operators to display gas level messages
def gasLevelAlert():
    if gasLevelGauge() == "Empty Tank":
        print("\033[1;31m  ***WARNING***\nGas tank is empty. \nCalling emergency contact(s)")

gasLevelAlert()