#!/bin/bash

<<<<<<< HEAD
start=$SECONDS
python3 featureSelector_alt.py regards_012916.csv 29977 Reg_Nsaids RC SF 5
python3 featureSelector_alt.py regards_012916.csv 29977 Reg_Nsaids RC SF 10
python3 featureSelector_alt.py regards_012916.csv 29977 Reg_Nsaids RC SF 15
python3 featureSelector_alt.py regards_012916.csv 29977 Reg_Nsaids RC SF 20
python3 featureSelector_alt.py regards_012916.csv 29977 Reg_Nsaids RC SF 70

python3 featureSelector_alt.py regards_012916.csv 29977 Reg_Nsaids RC SB 5
python3 featureSelector_alt.py regards_012916.csv 29977 Reg_Nsaids RC SB 10
python3 featureSelector_alt.py regards_012916.csv 29977 Reg_Nsaids RC SB 15
python3 featureSelector_alt.py regards_012916.csv 29977 Reg_Nsaids RC SB 20
python3 featureSelector_alt.py regards_012916.csv 29977 Reg_Nsaids RC SB 70

python3 featureSelector_alt.py regards_012916.csv 29977 Diabetes_SR RC SB 5
python3 featureSelector_alt.py regards_012916.csv 29977 Diabetes_SR RC SB 10
python3 featureSelector_alt.py regards_012916.csv 29977 Diabetes_SR RC SB 15
python3 featureSelector_alt.py regards_012916.csv 29977 Diabetes_SR RC SB 20
python3 featureSelector_alt.py regards_012916.csv 29977 Diabetes_SR RC SB 70

python3 featureSelector_alt.py regards_012916.csv 29977 death_indicator RC SF 5
python3 featureSelector_alt.py regards_012916.csv 29977 death_indicator RC SF 10
python3 featureSelector_alt.py regards_012916.csv 29977 death_indicator RC SF 15
python3 featureSelector_alt.py regards_012916.csv 29977 death_indicator RC SF 20
python3 featureSelector_alt.py regards_012916.csv 29977 death_indicator RC SF 70

python3 featureSelector_alt.py regards_012916.csv 29977 death_indicator RC SB 5
python3 featureSelector_alt.py regards_012916.csv 29977 death_indicator RC SB 10
python3 featureSelector_alt.py regards_012916.csv 29977 death_indicator RC SB 15
python3 featureSelector_alt.py regards_012916.csv 29977 death_indicator RC SB 20
python3 featureSelector_alt.py regards_012916.csv 29977 death_indicator RC SB 70

python3 featureSelector_alt.py regards_012916.csv 29977 Stroke_SR RC SF 5
python3 featureSelector_alt.py regards_012916.csv 29977 Stroke_SR RC SF 10
python3 featureSelector_alt.py regards_012916.csv 29977 Stroke_SR RC SF 15
python3 featureSelector_alt.py regards_012916.csv 29977 Stroke_SR RC SF 20
python3 featureSelector_alt.py regards_012916.csv 29977 Stroke_SR RC SF 70

python3 featureSelector_alt.py regards_012916.csv 29977 Stroke_SR RC SB 5
python3 featureSelector_alt.py regards_012916.csv 29977 Stroke_SR RC SB 10
python3 featureSelector_alt.py regards_012916.csv 29977 Stroke_SR RC SB 15
python3 featureSelector_alt.py regards_012916.csv 29977 Stroke_SR RC SB 20
python3 featureSelector_alt.py regards_012916.csv 29977 Stroke_SR RC SB 70




=======
start = $SECONDS
python featureSelector_alt.py regards_012916.csv 29977 Alcohol_use_current RC SF 5
python featureSelector_alt.py regards_012916.csv 29977 Reg_Nsaids RC SF 5
python featureSelector_alt.py regards_012916.csv 29977 Smoke_current RC SF 5
python featureSelector_alt.py regards_012916.csv 29977 Diabetes_SR RC SF 5
python featureSelector_alt.py regards_012916.csv 29977 death_indicator RC SF 5
python featureSelector_alt.py regards_012916.csv 29977 Stroke_SR RC SF 5
duration= $(( SECONDS - start ))
echo "Completed in $SECONDS seconds"
>>>>>>> 0e3a714f40a6c71129c0f52cb43aa3046ba766ea
