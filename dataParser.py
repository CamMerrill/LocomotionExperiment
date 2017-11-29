from os import walk


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

for item in files:
	itemName = item.split(".")[0]
	inputFile = open("Logs/" + item, 'r')
	outputFile = open("Logs/Parsed/" + itemName + "-parsed.csv", 'w')
	outputFile.write("hi")
	

	












