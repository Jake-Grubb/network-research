# Programmer: Jacob Grubb (jagrubb@siue.edu)
# Project: Continuity Experiment
# Organization: SIUE CS Department
# Date: July 2019
# File: evaluate.py


import numpy as np
import pandas as pd
import sys
import os
import time
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

def main():
	#Take arguments as an input
	if(len(sys.argv) != 3):
		print("Invalid Syntax!\nCorrect Syntax: evaluate.py <data directory> <num-features>")
		exit(1)

	#Identify all files within the given directory
	directory = sys.argv[1]
	num_features = int(sys.argv[2])
	names = range(num_features)
	listOfFiles = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
	#For each file in the directory, we run k-nearest-neighbors and time it
	for file in listOfFiles:
		#Load file
		dataset = pd.read_csv(directory + file, names=names)
		#Start time
		print("\nTesting: " + directory + file + "\n")
		start_time = time.time()
		run_k_means(dataset)
		end_time = time.time()
		with open("./output.txt", "a") as outFile:
			outFile.write(file + ", " + str(end_time - start_time) + "\n")


def run_k_means(dataset):
	#We will assume the first column is our attribute
	#All other columns are attributes
	x = dataset.iloc[:,1:].values #AKA x
	y = dataset.iloc[:,0].values # AKA y
	#Split into test and train
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)
	#Train the classifier
	classifier = KNeighborsClassifier(n_neighbors=5)
	classifier.fit(x_train, y_train)
	#Make our predicitions
	y_pred = classifier.predict(x_test)
	#Run our evaluation
	print(confusion_matrix(y_test, y_pred))
	print(classification_report(y_test, y_pred))

main()


