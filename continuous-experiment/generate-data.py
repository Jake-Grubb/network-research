# Programmer: Jacob Grubb
# Project: Continuity Experiment
# Organization: SIUE CS Department
# File: generate-data.py
# Date: July 2019

import sys
import random
import csv

def generate_csv():
	if(len(sys.argv) != 4):
		print("Invalid Syntax: Correct Syntax:\ngenerate-data <numBinary> <totalFeatures> <numEntries>")
		exit(0)
	#Get parameters (int numBinary, int totalFeatures, int numEntries)
		#numDiscrete =: Number of features with binary values (0, 1)
	numDiscrete = int(sys.argv[1])
		#totalFeatures =: Total number of features (columns)
	totalFeatures = int(sys.argv[2])
		#numEntries =: Total number of entries (rows)
	numEntries = int(sys.argv[3])

	dataArray = []
	#for each number in range(0, numEntries)
	for num in range(numEntries):
		#generate an entry in of the form
		row = []
		# row = [0 ... numDiscrete] + [numdiscrete + 1 ... totalFeatures]
		for feature in range(numDiscrete):
			row.append(random.randrange(2))
		for feature in range(totalFeatures - numDiscrete):
			row.append(random.random())
		dataArray.append(row)
	with open('./' + str(numDiscrete) + '_' + str(totalFeatures) + '_' + str(numEntries) + '.csv', 'w') as outFile:
		outWriter = csv.writer(outFile)
		for row in dataArray:
			outWriter.writerow(row)
	return

def generate_out():
	if(len(sys.argv) != 4):
		print("Invalid Syntax: Correct Syntax:\ngenerate-data <numBinary> <totalFeatures> <numEntries>")
		exit(0)
	#Get parameters (int numBinary, int totalFeatures, int numEntries)
	numDiscrete = int(sys.argv[1])
		#numDiscrete =: Number of features with binary values (0, 1)
	totalFeatures = int(sys.argv[2])
		#totalFeatures =: Total number of features (columns)
	numEntries = int(sys.argv[3])
		#numEntries =: Total number of entries (rows)
	dataArray = []
	#for each number in range(0, numEntries)
	for num in range(numEntries):
		#generate an entry in of the form
		row = []
		for feature in range(numDiscrete):
			row.append(random.randrange(2))
		for feature in range(totalFeatures - numDiscrete):
			row.append(random.random())
		# row = [0 ... numDiscrete] + [numdiscrete + 1 ... totalFeatures]
		dataArray.append(row)
	return dataArray

