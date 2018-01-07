#!/usr/bin/env python
from os import walk
import math
import statistics
import numpy as np

#We need to import the raw data from logs again to prune for outliers



def outliers_modified_z_score(ys):
        threshold = 7
        median_y = np.median(ys)
        median_absolute_deviation_y = np.median([np.abs(y - median_y) for y in ys])
        modified_z_scores = [0.6745 * (y - median_y) / median_absolute_deviation_y
                            for y in ys]
        return np.where(np.abs(modified_z_scores) > threshold)

def outliers_iqr(ys):
        quartile_1, quartile_3 = np.percentile(ys, [25, 75])
        iqr = quartile_3 - quartile_1
        lower_bound = quartile_1 - (iqr * 1.5)
        upper_bound = quartile_3 + (iqr * 1.5)
        print(lower_bound, upper_bound)
        return np.where((ys > upper_bound))

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
    prevX = 0
    prevY = 0
    xList = []
    yList = []
    xDistList = []
    yDistList = []
    euclList = []

    #Parsed the actual file now
    #We're gonna need to do this twice lol
    for line in inputFile:
        lineSplit = line.split(" ")
        lineX = float(lineSplit[0])
        lineY = float(lineSplit[1])
        lineT = float(lineSplit[2])
        if count != 0:
            deltaX = abs(lineX-prevX)
            deltaY = abs(lineY-prevY)
            xDistList.append(deltaX)
            yDistList.append(deltaY)
            euclList.append(math.sqrt(math.pow(deltaX,2) + math.pow(deltaY,2)))
        #Lets try without sign
        totalX = totalX + lineX
        totalY = totalY + lineY
        prevX = lineX
        prevY = lineY
        xList.append(lineX)
        yList.append(lineY)
        #print cause lazy
        count += 1

            


print("File: " + itemName)
print("Total X: " + str(totalX))
print("Total Y: " + str(totalY))

#NOW WE NEED TO DO +/- 3 STD DEVIATIONS AND REMOVEEEEE THEM
#SAMPLE STANDARD DEVIATION
x_result = outliers_modified_z_score(xList)
y_result = outliers_modified_z_score(yList)
union = set(x_result[0]).union(y_result[0])
print(union)
for item in union:
    print(euclList[item])
for item in union:
    xList.pop(item)
    yList.pop(item)

print(len(xList))
print(len(yList))

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
