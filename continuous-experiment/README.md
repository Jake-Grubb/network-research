# Continuity Experiment


## Goals
Determine the effects of discrete versus continuous data when running k-nearest neighbors in terms of runtime.

## Testing Methodology
Generate a number of datasets. Each set of data will have a constant amount of features (columns) and entries (rows).
The variable to be tested is the ratio of discrete to continuous data. Discrete data will be a binary whole number
(0 or 1), whereas all continuous data will be a decimal value between 0 and 1.

The datasets generated will be of the form

|Total Features | Discrete Features | Continuous Features | Time-to-complete|
|----|----|----|----|
|100|5|95|*|
|100|10|90|*|
|100|20|80|*|
|100|30|70|*|	
|100|50|50|*|
|100|70|30|*|
|100|100|0|*|
## Results
TO BE DETERMINED
