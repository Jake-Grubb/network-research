#Programmer: Jacob Grubb
#Organization: SIUE CS Department
#Project: scikit-learn clustering metrics
#File: metric.py

import sklearn.metrics as skm
import pandas
import sys


def main():
	if(len(sys.argv) != 3):
		print("Error: invalid syntax\nCorrect Syntax: python3 metric.py <input file> <metric-type>\nValid metric types: boul, silh")
		sys.exit(0)
	print("Reading file...")
	pfile = pandas.read_csv(sys.argv[1])
	print("Success")
	mode = sys.argv[2]
	if(mode != 'boul' and mode != 'silh'):
		print("Error: invalid syntax\nCorrect Syntax: python3 metric.py <input file> <metric-type>\nValid metric types: boul, silh")
		sys.exit(0)
	if(mode == 'boul'):
		runBoul(pfile)
	elif(mode == 'silh'):
		runSilh(pfile)
	return

def runBoul(pfile):
	skm.davies_bouldin_score(pfile.values, pfile.columns)
def runSilh(pfile):
	skm.silhouette_score(pfile.values, pfile.columns)
main()
