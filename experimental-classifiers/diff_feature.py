#Programmer: Jacob Grubb
#Organization: SIUE CS Department
#Project: experimental-classifiers
#File: diff_feature.py
#Description: Script for taking two output files and comparing selected features.

#List of Imports
import sys


#Open files from input
if(len(sys.argv) != 3):
	print("Invalid Parameters:\nCorrect: python3 diff_feature.py <First Results> <Second Results>")

file_one_name = sys.argv[1]
file_two_name = sys.argv[2]

with open(file_one_name, "r") as inFile_one:
	file_one_contents = inFile_one.read()

with open(file_two_name, "r") as inFile_two:
	file_two_contents = inFile_two.read()

print(file_one_contents)
