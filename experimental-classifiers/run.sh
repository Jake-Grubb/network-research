#!/bin/bash

start = $SECONDS
python featureSelector_alt.py regards_012916.csv 29977 Alcohol_use_current RC SF 5
python featureSelector_alt.py regards_012916.csv 29977 Reg_Nsaids RC SF 5
python featureSelector_alt.py regards_012916.csv 29977 Smoke_current RC SF 5
python featureSelector_alt.py regards_012916.csv 29977 Diabetes_SR RC SF 5
python featureSelector_alt.py regards_012916.csv 29977 death_indicator RC SF 5
python featureSelector_alt.py regards_012916.csv 29977 Stroke_SR RC SF 5
duration= $(( SECONDS - start ))
echo "Completed in $SECONDS seconds"
