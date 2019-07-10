# Continuity Experiment


## Goals
Determine the effects of discrete versus continuous data when running K-Nearest Neighbors in terms of runtime.

## Testing Methodology
Generate a number of datasets. Each set of data will have a constant amount of features (columns) and entries (rows).
The variable to be tested is the ratio of discrete to continuous data. Discrete data will be a binary whole number
(0 or 1), whereas all continuous data will be a decimal value between 0 and 1.

The datasets generated will be of the form

| Entries | K-Value |Total Features | Discrete Features | Continuous Features | Time-to-complete|
|----|----|----|----|----|----|
|20000|5|100|5|95|*|
|20000|5|100|10|90|*|
|20000|5|100|20|80|*|
|20000|5|100|30|70|*|	
|20000|5|100|50|50|*|
|20000|5|100|70|30|*|
|20000|5|100|100|0|*|

Following generation, each dataset will be ran through the Python Scikit-learn Library's implementation of K-Nearest Neighbors. Each data set is composed of 20,000 entries, which will be split into 75% training, 25% testing. For the purpose of standardized testing, K will be set to a value of 5 for the duration of these experiments. The time-to-complete will be measured as the time from the start of training to the end of testing.

Results will be in a similar table as shown above, with the Time-to-complete colummn completed. If there is a NEGATIVE trend between Time-to-complete and number of discrete features, we can conclude that K-nearest neighbors will run faster with more discrete features. Any other trend will prove inconclusive.

## Results
TO BE DETERMINED
