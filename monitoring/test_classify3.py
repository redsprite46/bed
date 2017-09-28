#!/usr/bin/python3
# encoding: utf-8

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics
from sklearn.externals import joblib

# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

if __name__ == "__main__":
    samples = pd.read_csv('C:/Users/ROBO-E-03/Desktop/scope/data/sample.csv', index_col=0)
    # X = samples[['acc', 'ch1', 'ch2', 'ch3', 'ch4', 'ch5']]
    X = samples[['ch1', 'ch2', 'ch3', 'ch4', 'ch5']]
    y = samples['state']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1)

    # classifier = MultinomialNB(alpha=0.2) # 63%
    # classifier = SVC() # 82%
    # classifier = SVC(kernel='linear', probability=True) # 86%
    # classifier = KNeighborsClassifier()   # 92%
    classifier = RandomForestClassifier()  # 95%
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    print(metrics.accuracy_score(y_test, y_pred))
    print(metrics.confusion_matrix(y_test, y_pred))
    # classifier = RandomForestClassifier()  # 95%
    classifier.fit(X, y)
    # joblib.dump(classifier, 'C:/Users/ROBO-E-03/Desktop/scope/data/cls_saito.pkl')

    # classifier = joblib.load('/home/ub/scope/data/cls_murosawa.pkl')