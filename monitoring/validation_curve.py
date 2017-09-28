import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.model_selection import validation_curve
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
"""
samples = pd.read_csv(
    'C:/Users/ROBO-E-03/Desktop/scope/data/sample.csv', index_col=0)
X = samples[["ch1", "ch2", "ch3", "ch4", "ch5", "ch6"]]
y = samples["state"]
param_range = [3, 4, 5, 6, 7, 8, 9, 10, 11]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1)
"""

train_samples = pd.read_csv(
    'C:/Users/ROBO-E-03/Desktop/scope/data/train_data.csv', index_col=0)
test_samples = pd.read_csv(
    'C:/Users/ROBO-E-03/Desktop/scope/data/test_data2.csv', index_col=0)
X_train = train_samples[['ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6']]
X_test = test_samples[['ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6']]
y_train = train_samples['state']
y_test = test_samples['state']
param_range = [3, 4, 5, 6, 7, 8, 9, 10, 11]

pipe_lr = Pipeline([("scl", StandardScaler()),
                    ("clf", KNeighborsClassifier())])

train_scores, test_scores = validation_curve(
    estimator=pipe_lr, X=X_train, y=y_train, param_name="clf__n_neighbors",
    param_range=param_range, cv=10)
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

plt.plot(param_range, train_mean, color="blue", marker="o",
         markersize=5, label="training accuracy")
plt.fill_between(param_range, train_mean + train_std, train_mean - train_std,
                 alpha=0.15, color="blue")
plt.plot(param_range, test_mean, color="green", linestyle="--", marker="s",
         markersize=5, label="validation accuracy")
plt.fill_between(param_range, test_mean + test_std, test_mean - test_std,
                 alpha=0.15, color="green")
plt.grid()
plt.xlabel("Neighbors")
plt.ylabel("Accuracy")
plt.legend(loc="lower right")
plt.ylim([0.5, 1.0])
plt.show()
