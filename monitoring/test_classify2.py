#!/usr/bin/python3
# encoding: utf-8

import pandas as pd
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier

if __name__ == "__main__":
    classifier = joblib.load('/home/ub/scope/data/cls_murosawa.pkl')
    samples = pd.read_csv('~/scope/data/sensor_per_sec.csv', index_col=0)
    X = samples[['ch1', 'ch2', 'ch3', 'ch4', 'ch5']]

    y_pred = classifier.predict(X)
    pred = pd.DataFrame(y_pred)
    pred.to_csv('~/scope/data/pred.csv')
