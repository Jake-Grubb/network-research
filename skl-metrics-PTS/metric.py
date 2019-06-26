#Programmer: Jacob Grubb
#Organization: SIUE CS Department
#Project: scikit-learn clustering metrics
#File: metric.py

import sklearn
import pandas
import sys


def main():
	if(len(sys.argv) != 3):
		print("Error: invalid syntax\n Correct Syntax: python3 metric.py <input file> <metric-type>\nValid metric types: bouldin, silhouette")
		sys.exit(0)
