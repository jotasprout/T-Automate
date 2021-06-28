# variable for date of next Friday?
# variables for date of next Monday and Tuesday?

# Function to make a date
# Convert date to string

# Function to concatinate landmass and date

import os

from secretVariables import *

def createWSR():
    for i in range(0,len(landmassReports)):
        for j in range(0, len(subsReports)):
            dirName = str(rootDir) + '/' + str(weeklyTasks[0]) + '/' + str(landmassReports[i]) + '/' + str(subsReports[j])

            if not os.path.exists(dirName):
                os.makedirs(dirName)
                print("Directory " , dirName, " created")
            else:
                print("Directory ", dirName, " already exists")

def createMinutes():
    for i in range(0,len(landmassMinutes)):
        for j in range(0, len(subsMinutes)):
            dirName = str(rootDir) + '/' + str(weeklyTasks[1]) + '/' + str(landmassMinutes[i]) + '/' + str(subsMinutes[j])

            if not os.path.exists(dirName):
                os.makedirs(dirName)
                print("Directory " , dirName, " created")
            else:
                print("Directory ", dirName, " already exists")

createWSR() 
createMinutes()                