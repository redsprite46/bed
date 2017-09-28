#!/usr/bin/python3
# coding: utf-8

from sklearn.model_selection import train_test_split
from sklearn.grid_search import GridSearchCV
import pandas as pd

# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

samples = pd.read_csv('C:/Users/ROBO-E-03/Desktop/scope/data/sample.csv', index_col=0)
X = samples[["ch1", "ch2", "ch3", "ch4", "ch5"]]
y = samples["state"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

