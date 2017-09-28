#!/usr/bin/python3
# encoding: utf-8

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
from sequential_backward_selection import SBS
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline

from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

if __name__ == "__main__":
    samples = pd.read_csv(
        'C:/Users/ROBO-E-03/Desktop/scope/data/sample.csv', index_col=0)
    # X = samples[['acc', 'ch1', 'ch2', 'ch3', 'ch4', 'ch5']]
    X = samples[['ch1', 'ch2', 'ch3', 'ch4', 'ch5']]
    # X = samples[['ch1', 'ch2', 'ch3', 'ch4']]
    y = samples['state']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1)

    # 標準化（ランダムフォレストの場合は必要ない）
    
    stdsc = StandardScaler()
    X_train_std = stdsc.fit_transform(X_train)
    X_test_std = stdsc.transform(X_test)
    

    # 特徴量の個数による影響の確認
    """
    knn = KNeighborsClassifier()
    sbs = SBS(knn, k_features=1)
    sbs.fit(X_train_std, y_train)
    k_feat = [len(k) for k in sbs.subsets_]
    plt.plot(k_feat, sbs.scores_, marker="o")
    plt.ylim([0.5, 1.1])
    plt.ylabel("Accuracy")
    plt.xlabel("Number of features")
    plt.grid()
    plt.show()

    knn.fit(X_train_std, y_train)
    print(knn.score(X_train_std, y_train))
    print(knn.score(X_test_std, y_test))
    """

    # classifier = MultinomialNB(alpha=0.2) # 63%
    # classifier = SVC() # 82%
    # classifier = SVC(kernel='linear', probability=True) # 86%
    # classifier = KNeighborsClassifier()   # 92%
    classifier = RandomForestClassifier(n_jobs=-1)  # 95%
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    print(metrics.accuracy_score(y_test, y_pred))
    print(metrics.confusion_matrix(y_test, y_pred))

    # 特徴量の重要度
    """feat_labels = ['ch1', 'ch2', 'ch3', 'ch4', 'ch5']
    importances = classifier.feature_importances_
    indices = np.argsort(importances)[::-1]
    for f in range(X_train.shape[1]):
        print("%2d) %-*s%f" %
              (f + 1, 30, feat_labels[indices[f]], importances[indices[f]]))
    """

    buf = pd.DataFrame(metrics.confusion_matrix(y_test, y_pred))
    buf.index = ["仰臥位", "右臥位", "左臥位", "長座位", "短座位", "端座位", "離床"]

    records = []
    accuracy = ["" for i in range(8)]
    accuracy[0:2] = ["accuracy", metrics.accuracy_score(y_test, y_pred)]
    records.append(accuracy)
    space = ["" for i in range(8)]
    records.append(space)
    subject = ["" for i in range(8)]
    subject[0] = "confusion_matrix"
    records.append(subject)
    data_head = ["", "仰臥位", "右臥位", "左臥位", "長座位",
                 "短座位", "端座位", "離床"]
    records.append(data_head)

    for index, row in buf.iterrows():
        rec = [index, row[0], row[1], row[2], row[3], row[4], row[5], row[6]]
        records.append(rec)

    result = pd.DataFrame(records)
    result.to_csv("C:/Users/ROBO-E-03/Desktop/scope/data/result.csv",
                  header=False, index=False)

    # classifier = RandomForestClassifier()  # 95%
    classifier.fit(X, y)
    # joblib.dump(classifier, 'C:/Users/ROBO-E-03/Desktop/scope/data/cls_saito.pkl')

    # classifier = joblib.load('/home/ub/scope/data/cls_murosawa.pkl')
