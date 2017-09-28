#!/usr/bin/python3
# encoding: utf-8

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

from sequential_backward_selection import SBS

if __name__ == "__main__":
    train_samples = pd.read_csv(
        'C:/Users/ROBO-E-03/Desktop/scope/data/sample.csv',
        index_col=0)
    test_samples = pd.read_csv(
        'C:/Users/ROBO-E-03/Desktop/scope/data/test1.csv', index_col=0)
    X_train = train_samples[['ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6']]
    X_test = test_samples[['ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6']]
    # X_train = train_samples[['ch1', 'ch2', 'ch3', 'ch4', 'ch5']]
    # X_test = test_samples[['ch1', 'ch2', 'ch3', 'ch4', 'ch5']]
    y_train = train_samples['state']
    y_test = test_samples['state']

    classifier1 = MultinomialNB(alpha=0.2) # 63%
    classifier2 = SVC() # 82%
    classifier3 = SVC(kernel='linear', probability=True) # 86%
    classifier4 = KNeighborsClassifier(n_neighbors=7)   # 92%
    classifier5 = RandomForestClassifier(n_jobs=-1)  # 95%

    pipe2 = Pipeline([("scl", StandardScaler()), ("clf", classifier2)])
    pipe3 = Pipeline([("scl", StandardScaler()), ("clf", classifier3)])
    pipe4 = Pipeline([("scl", StandardScaler()), ("clf", classifier4)])

    clf_labels = ["NB", "SVC_rbf", "SVC_linear", "KNN", "RF"]
    all_classifier = [classifier1, pipe2, pipe3, pipe4, classifier5]

    for label, clf in zip(clf_labels, all_classifier):
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)

        print(label)
        print(metrics.accuracy_score(y_test, y_pred))
        print(metrics.confusion_matrix(y_test, y_pred), "\n")

        buf = pd.DataFrame(metrics.confusion_matrix(y_test, y_pred))
        buf.index = ["臥位", "長座位", "短座位", "端座位", "離床"]

        records = []
        data_head = ["", "臥位", "長座位", "短座位", "端座位", "離床"]
        title = ["" for i in range(len(data_head))]
        title[0:1] = [label]
        records.append(title)
        accuracy = ["" for i in range(len(data_head))]
        accuracy[0:2] = ["accuracy", metrics.accuracy_score(y_test, y_pred)]
        records.append(accuracy)
        subject = ["" for i in range(len(data_head))]
        subject[0] = "confusion_matrix"
        records.append(subject)
        records.append(data_head)

        for index, row in buf.iterrows():
            rec = [index, row[0], row[1], row[2], row[3], row[4]]
            records.append(rec)

        result = pd.DataFrame(records)
        path = "C:/Users/ROBO-E-03/Desktop/scope/data/result_" + label + ".csv"
        result.to_csv(path, header=False, index=False)

    # classifier = RandomForestClassifier()  # 95%
    # classifier.fit(X, y)
    # joblib.dump(classifier, 'C:/Users/ROBO-E-03/Desktop/scope/data/cls_saito.pkl')

    # classifier = joblib.load('/home/ub/scope/data/cls_murosawa.pkl')
