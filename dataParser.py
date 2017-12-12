from os import walk
import math

#Raw Data in Logs/*
#We are converting the raw Data from the Wii Balance board (position data) into center of pressure total path length
#Each trial is stored individually, so we need to get all the files in the Log directory.

files = []
for (dirpath, dirnames, filenames) in walk('Logs'):
	files.extend(filenames)
	break

filesPruned = []

for item in files:
	splitItem = item.split(".")
	if splitItem[1] == "csv":
		filesPruned.append(item)

files = filesPruned
#We now have a list of all csv files in Logs directory, pruning out excess files in a roundabout way

#for each file we need an I and O

masterFile = open("master-cop-eucl.csv", 'w')
masterFile.write("FileName, Total X, Total Y, Total D, Total T, Distance, Samples\n")

for item in files:
	itemName = item.split(".")[0]
	inputFile = open("Logs/" + item, 'r')
	outputFile = open("Logs/Parsed/" + itemName + "-parsed.csv", 'w')
	outputFile.write("X Pos, Y Pos, Time, dT, dX Pos, dY Pos,,Samples, Total X, Total Y, Total Time, Total D+\n")
	count = 0
	totalX = 0
	totalY = 0
	totalT = 0
	totalD = 0
	for line in inputFile:
		lineSplit = line.split(" ")
		lineX = float(lineSplit[0])
		lineY = float(lineSplit[1])
		lineT = float(lineSplit[2])
		if count != 0:
			totalX = totalX + abs(lineX - prevX)
			totalY = totalY + abs(lineY - prevY)
			totalT = totalT + abs(lineT - prevT)
			x_valu = abs(lineX - prevX)
			y_valu = abs(lineY - prevY)
			totalD = totalD + math.sqrt(math.pow(x_valu,2) + math.pow(y_valu,2))
		prevX = float(lineSplit[0])
		prevY = float(lineSplit[1])
		prevT = float(lineSplit[2])
		count = count + 1
	
	outputFile.write("X Pos, Y Pos, Time, dT, dX Pos, dY Pos,," + str(count) + "," + str(totalX) + "," + str(totalY) + "," + str(totalT) + "," + str(totalX+totalX))
	masterFile.write(item.split(".")[0] + "," + str(totalX) + "," + str(totalY) + "," + str(totalX + totalY) + "," + str(totalT) + "," + str(totalD) + "," + str(count) + "\n")

