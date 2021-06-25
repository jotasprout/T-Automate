# variable for date of next Friday?
# variables for date of next Monday and Tuesday?

# Function to make a date
# Convert date to string

# Function to concatinate landmass and date

import os

from secretVariables import *

def createWSR():
    for i in range(0,len(landmassReports)):
        for j in range(0, len(landmassSubs)):
            dirName = str(rootDir) + '/' + str(weeklyTasks[0]) + '/' + str(landmassReports[i]) + '/' + str(landmassSubs[j])

            if not os.path.exists(dirName):
                os.makedirs(dirName)
                print("Directory " , dirName, " created")
            else:
                print("Directory ", dirName, " already exists")

def createMinutes():
    for i in range(0,len(landmassMinutes)):
        for j in range(0, len(landmassSubs)):
            dirName = str(rootDir) + '/' + str(weeklyTasks[1]) + '/' + str(landmassMinutes[i]) + '/' + str(landmassSubs[j])

            if not os.path.exists(dirName):
                os.makedirs(dirName)
                print("Directory " , dirName, " created")
            else:
                print("Directory ", dirName, " already exists")

createWSR() 
createMinutes()                