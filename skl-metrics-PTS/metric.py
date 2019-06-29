#Programmer: Jacob Grubb
#Organization: SIUE CS Department
#Project: scikit-learn clustering metrics
#File: metric.py

import sklearn.metrics as skm
import pandas
import sys

def main():
	if(len(sys.argv) != 4):
		print("Error: invalid syntax\nCorrect Syntax: python3 metric.py <input file> <metric-type> <target column>\nValid metric types: boul, silh")
		sys.exit(0)
	print("Reading file...")
	pfile = pandas.read_csv(sys.argv[1])
	pfile = pfile.drop(pfile.index[0])
	print("Success")
	mode = sys.argv[2]
	target_column = sys.argv[3]
	if(mode != 'boul' and mode != 'silh'):
		print("Error: invalid syntax\nCorrect Syntax: python3 metric.py <input file> <metric-type>\nValid metric types: boul, silh")
		sys.exit(0)
	if(mode == 'boul'):
		value = runBoul(pfile, target_column)
	elif(mode == 'silh'):
		value = runSilh(pfile, target_column)
	with open("./" + sys.argv[1] + "_" + mode + "_results.txt", "w") as outFile:
		outFile.write("mode " + "value: " + str(value))
	return

def runBoul(pfile, results_name):
	results_column = pfile[results_name]
	pfile.drop(results_name, axis=1, inplace = True)
	return skm.davies_bouldin_score(pfile, results_column)
def runSilh(pfile, results_name):
	results_column = pfile[results_name]
	pfile.drop(results_name, axis=1, inplace = True)
	return skm.silhouette_score(pfile, results_column)
main()
