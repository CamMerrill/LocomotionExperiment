from os import walk
import math
import statistics
import numpy as np
from statsmodels import robust

files = []
for (dirpath,dirnames, filenames) in walk('Rotations-Removed/'):
    files.extend(filenames)
    break
filesPruned = []
for item in files:
    splitItem = item.split(".")
    if splitItem[1] == "csv":
        filesPruned.append(item)
files = filesPruned
outFile = open("catalog-rot.csv", 'w')
for item in files:
    itemName = item.split(".")[0]
    inputFile = open("Rotations-Removed/"+ item, 'r')
    count = 0
    totalX = 0
    totalY = 0
    totalT = 0
    prevX = 0
    prevY = 0
    totalEucl = 0
    xList = []
    yList = []
    euclList = []
    print(item)
    for line in inputFile:
        lineSplit = line.split(",")
        lineX = float(lineSplit[0])
        lineY = float(lineSplit[1])
        if count != 0:
            deltaX = abs(lineX - prevX)
            deltaY = abs(lineY - prevY)
            totalX = totalX + deltaX
            totalY = totalY + deltaY
            totalEucl = totalEucl + math.sqrt(math.pow(deltaX,2) + math.pow(deltaY,2))
        count = count + 1
        prevX = lineX
        prevY = lineY
    outFile.write(itemName + "," + str(totalX) + "," + str(totalY) + "," + str(totalEucl) + "\n")





