from os import walk
import math
import matplotlib.pyplot as plt

#Get All Logs, again

files = []
for (dirpath, dirnames, filenames) in walk('../Logs'):
	files.extend(filenames)
	break
filesPruned = []
for item in files:
	splitItem = item.split(".")
	if splitItem[1] == "csv":
		filesPruned.append(item)

files = filesPruned #lazy copy

#Now we have a list of all csv files, lets prune
maxX = 0
maxY = 0
previousSubject = 1
for item in files:
	inputFile = open("../Logs/" + item, 'r')
	
	#output file goes here, probably
	#outputfile
	xVals = []
	yVals = []

	for line in inputFile:
		lineSplit = line.split(" ")
		lineX = float(lineSplit[0])
		lineY = float(lineSplit[1])
		if abs(lineX) > maxX:
			maxX = abs(lineX)
		if abs(lineY) > maxY:
			maxY = abs(lineY)

		xVals.append(lineX)
		yVals.append(lineY)

		#NEED TO DRAW


	currentSubject = item[0]
	if currentSubject != previousSubject:
		plt.savefig("Figures/Normalized/" + currentSubject + ".png")
		plt.clf()
		plt.figure(currentSubject)
		count = 0
	plt.subplot(count)
	plt.plot(xVals, yVals, linewidth=0.5)
	plt.title(item)
	plt.axis([-200, 200, -125, 125])
	previousSubject = currentSubject
	#plt.show()
	#plt.savefig("Figures/Normalized/" + item[:-4] + ".png")

print (maxX, maxY)
