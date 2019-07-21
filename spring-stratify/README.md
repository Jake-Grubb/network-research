# Continuity Experiment


## Goals
Experiment to evaluate the effects of proper stratification of datasets when running clustering functions.

## Testing Methodology

The script provided by the previous researcher's work will be slightly modified, adding a parameter to the "train_test_split" function: "stratify=data[targetcolumn]". This will ensure that the target column will be stratified properly between the training and testing set. Following these modifications, all combinations of the following will be tested:

* Classification Type
  * Step Forward
  * Step Backward
* k Value
  * 5
  * 10
  * 15
  * 20
  * 70
* Classifier 
  * Naive Bayes
  * Logistic Regression
  * Random Forest
* Target Feature
  * Current Alchol Use
  * Deceased, Diabetic
  * Regular NSAID Usage
  * Current Smoker
  * Reported Stroke

This will provide a total of 360 tests, which will be compared with the previous results AUC scores, while noting the selected features, to identify any distinctions between the non-stratified input and the stratified input. A distinction is defined as a difference of more than 0.01 AUC and/or a different set of selected features.

## Results

To be determined.
