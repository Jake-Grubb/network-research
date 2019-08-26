# Project: heavy-drinking
# Programmer: Jacob Grubb
# Organization: SIUE CS Department
# File: modify-data.py
# Description: Python script for modifying the existing REGARDS dataset, adding new features for testing against.


import csv
import sys


if(len(sys.argv) != 3):
	print("Invalid syntax\nCorrect syntax: python3 modify-data.py <source-file> <target-file>")
	exit(1)

inputFileName = sys.argv[1]
outputFileName = sys.argv[2]


with open(inputFileName) as inFile:
	fileReader = csv.DictReader(inFile)
	with open(outputFileName, 'w') as outFile:
		headernames = fileReader.fieldnames + ['heavy_alcohol_risk','light_alcohol_risk']
		fileWriter = csv.DictWriter(outFile, fieldnames=headernames)
		fileWriter.writeheader()
		#for row in fileReader:
		#	if(row['Alc_Drinks_Wk'] == 1):
		#		print(row['Alc_Drinks_Wk'])
		for row in fileReader:
			if(row['Alc_Drinks_Wk'] == ""): #Upon empty, skip
				row['heavy_alcohol_risk'] = 0
				row['light_alcohol_risk'] = 0
			elif((float(row['Alc_Drinks_Wk']) * 224) > 35 and row['Gender'] == '1'): #High abuse, male
				row['heavy_alcohol_risk'] = 1
				row['light_alcohol_risk'] = 0
				fileWriter.writerow(row)
			elif((float(row['Alc_Drinks_Wk']) * 224) > 28 and row['Gender'] == '0'): #High abuse, female
				row['heavy_alcohol_risk'] = 1
				row['light_alcohol_risk'] = 0
				fileWriter.writerow(row)
			elif((float(row['Alc_Drinks_Wk']) * 224) > 14 and row['Gender'] == '1'): #Moderate abuse, male
				row['heavy_alcohol_risk'] = 0
				row['light_alcohol_risk'] = 1
				fileWriter.writerow(row)
			elif((float(row['Alc_Drinks_Wk']) * 224) > 7 and row['Gender'] == '0'): #Moderate abuse female
				row['heavy_alcohol_risk'] = 0
				row['light_alcohol_risk'] = 1
				fileWriter.writerow(row)
			else:
				row['heavy_alcohol_risk'] = 0
				row['light_alcohol_risk'] = 0
				fileWriter.writerow(row)
