#!/usr/bin/env python
from os import walk
import math

#We need to import the raw data from logs again to prune for outliers


files = []
for (dirpath, dirnames, filenames) in walk('../Logs'): #DIRECTORY SPECIFIC!
    files.extend(filenames)
    break
filesPruned = []

for item in files:
    splitItem = item.split(".")
    if splitItem[1] == "csv":
        filesPruned.append(item)
files = filesPruned
#Alright we know have a list of all csv files in the Logs directory.
#First, we need to traverse the file to find mean, and std deviation for a given trial

print(files)
files = ["11-A.csv"]
for item in files:
    itemName = item.split(".")[0]
    inputFile = open("../Logs/" + item, 'r')
    #outputFile = open("Logs/Parsed/" + itemName + "-outliers-pruned.csv", 'w')
    count = 0
    #Lets total the values up again, probably useful
    totalX = 0
    totalY = 0
    totalT = 0
    #Parsed the actual file now
    #We're gonna need to do this twice lol
    for line in inputFile:
        lineSplit = line.split(" ")
        lineX = float(lineSplit[0])
        lineY = float(lineSplit[1])
        lineT = float(lineSplit[2])
        #Lets try without sign
        totalX = totalX + lineX
        totalY = totalY + lineY
        #print cause lazy


print("File: " + itemName)
print("Total X: " + str(totalX))
print("Total Y: " + str(totalY))

#NOW WE NEED TO DO +/- 3 STD DEVIATIONS AND REMOVEEEEE THEM





# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
