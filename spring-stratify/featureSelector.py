# Wrapper Methods for Feature Selection

import sys
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_selection import VarianceThreshold

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import roc_auc_score

from mlxtend.feature_selection import SequentialFeatureSelector
from mlxtend.feature_selection import ExhaustiveFeatureSelector

dataset_fname = sys.argv[1]
num_records = int(sys.argv[2])
target_column = str(sys.argv[3])
classifier_name = str(sys.argv[4])
wrapper_method_name = str(sys.argv[5])
num_selected_features = int(sys.argv[6])

ofile_name = "output_" + classifier_name + "_" + wrapper_method_name + "_" + target_column + "_" + sys.argv[6] + ".txt"

results_file = open(ofile_name, "a")

regards_data = pd.read_csv(dataset_fname, nrows=num_records)

num_columns = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64', 'float128']

numerical_columns = list(regards_data.select_dtypes(include=num_columns).columns)
regards_data = regards_data[numerical_columns]
results_file.write('\nShapes are printed in the format (rows, columns)')
results_file.write('\nregards_data.shape:\n')
np.savetxt(results_file, regards_data.shape)

train_features, test_features, train_labels, test_labels = train_test_split(
    regards_data.drop(labels=target_column, axis='columns'),
    regards_data[target_column],
    test_size=0.2,
    random_state=41)

correlated_features = set()
correlated_features_complement = set()
correlation_matrix = regards_data.corr()
for i in range(len(correlation_matrix.columns)):
	for j in range(i):
		if abs(correlation_matrix.iloc[i, j]) > 0.8:
			column_name = correlation_matrix.columns[i]
			correlated_features.add(column_name)

			complement_name = correlation_matrix.columns[j]
			correlated_features_complement.add(complement_name)

results_file.write('\nRemoved correlated_features:\n')
for item in correlated_features:
	results_file.write("%s\n" % item)

results_file.write('\nFeatures were correlated with:\n')
for item in correlated_features_complement:
	results_file.write("%s\n" % item)

train_features.drop(labels=correlated_features, axis='columns', inplace=True)
test_features.drop(labels=correlated_features, axis='columns', inplace=True)

results_file.write('\ntrain_features.shape:\n')
np.savetxt(results_file, train_features.shape)
results_file.write('\ntest_features.shape:\n')
np.savetxt(results_file, test_features.shape)

clf = LogisticRegression(random_state=0)
if (classifier_name == "NB"):
	clf = GaussianNB()
elif (classifier_name == "RF"):
	clf = RandomForestClassifier(n_jobs=-1)
elif (classifier_name == "KNN"):
	clf = KNeighborsClassifier(n_neighbors=4)

if (wrapper_method_name != "EX"):
	# Step forward or backward feature selection
	direction = (wrapper_method_name == "SF")

	feature_selector = SequentialFeatureSelector(clf,
                                                 k_features=num_selected_features,
                                                 forward=direction,
                                                 verbose=2,
                                                 scoring='roc_auc',
                                                 cv=4)
else:
	# Exhaustive feature selection
	feature_selector = ExhaustiveFeatureSelector(clf,
                                                 min_features=5,
                                                 max_features=num_selected_features,
                                                 scoring='roc_auc',
                                                 print_progress=True,
                                                 cv=2)

features = feature_selector.fit(np.array(train_features.fillna(0)), train_labels)
    
filtered_features = train_features.columns[list(features.k_feature_idx_)]
results_file.write('\n\nfiltered_features for %s:\n' % target_column)
for item in filtered_features:
	results_file.write("%s\n" % item)

clf = LogisticRegression(random_state=0)
if (classifier_name == "NB"):
	clf = GaussianNB()
elif (classifier_name == "RF"):
	clf = RandomForestClassifier(n_estimators=100, random_state=41, max_depth=3)
elif (classifier_name == "KNN"):
	clf = KNeighborsClassifier(n_neighbors=4)

clf.fit(train_features[filtered_features].fillna(0), train_labels)

train_prediction = clf.predict_proba(train_features[filtered_features].fillna(0))
results_file.write('\nROC-AUC on training set: {}'.format(roc_auc_score(train_labels, train_prediction[:, 1])))

test_prediction = clf.predict_proba(test_features[filtered_features].fillna(0))
results_file.write('\nROC-AUC on test set: {}'.format(roc_auc_score(test_labels, test_prediction[:, 1])))

results_file.close()
