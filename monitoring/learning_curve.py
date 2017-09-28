import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

samples = pd.read_csv(
    'C:/Users/ROBO-E-03/Desktop/scope/data/sample.csv', index_col=0)
X = samples[["ch1", "ch2", "ch3", "ch4", "ch5"]]
y = samples["state"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1)

classifer = KNeighborsClassifier()
pipe = Pipeline([("scl", StandardScaler()), ("clf", classifer)])

train_sizes, train_scores, test_scores = learning_curve(
    estimator=pipe, X=X_train, y=y_train,
    train_sizes=np.linspace(0.1, 1.0, 10), n_jobs=1)
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

plt.plot(train_sizes, train_mean, color="blue", marker="o",
         markersize=5, label="training accuracy")
plt.fill_between(train_sizes, train_mean + train_std, train_mean - train_std,
                 alpha=0.15, color="blue")
plt.plot(train_sizes, test_mean, color="green", linestyle="--", marker="s",
         markersize=5, label="validation accuracy")
plt.fill_between(train_sizes, test_mean + test_std, test_mean - test_std,
                 alpha=0.15, color="green")
plt.grid()
plt.xlabel("Number of training samples")
plt.ylabel("Accuracy")
plt.legend(loc="lower right")
plt.ylim([0.5, 1.0])
plt.show()
