import random

# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty Tank", "Quarter Tank", "Half Tank", "3 Quarters Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    print(currentGasLevel)

gasLevelGauge()