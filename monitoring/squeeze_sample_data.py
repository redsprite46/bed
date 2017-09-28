#!/usr/bin/python3
# encoding: utf-8

import pandas as pd

if __name__ == "__main__":
    samples = pd.read_csv('~/scope/data/sample.csv', index_col=0)

    results = []
    for index, row in samples.iterrows():
        if max(row[['ch1', 'ch2', 'ch3', 'ch4', 'ch5']]) < 0.1:
            continue
        if row['state'] == 'g':
            continue
        results.append(row)

    new_samples = pd.DataFrame(results)
    new_samples.columns = ['time', 'state', 'acc',
         'ch1', 'ch2', 'ch3', 'ch4', 'ch5']
    new_samples.to_csv('~/scope/data/sample1.csv')

    # X = samples[['acc', 'ch1', 'ch2', 'ch3', 'ch4', 'ch5']]
    # X = samples[['ch1', 'ch2', 'ch3', 'ch4', 'ch5']]
    # y = samples['state']
