# Cancer Patient Prediction
ECE143 final project  
Author: Hung-Te Cheng, Aleksander Banaszczyk, Dhruv Chaddah, Jordan Taylor, Jieru Bai

## File Structure
```console
├── train.py
├── data_preprocessing.py
├── plot_histogram.py
├── data_split.py
├── data
│   └── cancer patient data sets.csv
└── img
    ├── corr.png
    ├── hist.png
    ├── hist_Age.png
    ├── weights_lr.png
    ├── weights_xgb.png
    └── weights_svm.png
```
```data/``` is where the dataset locates and ```img/``` is where generated plots store

## Prerequisite 3rd-party Modules
- numpy
- pandas
- matplotlib
- sklearn
- seaborn
- xgboost

## Execution
### Train all models without giving extra arguments
```console
foo@bar:~$ python train.py
```
### Train specific models by giving argument
- Logistic Regression
```console
foo@bar:~$ python train.py lr
```
- XGBClassifier
```console
foo@bar:~$ python train.py xgb
```
- SVM
```console
foo@bar:~$ python train.py svm
```
