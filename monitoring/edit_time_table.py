#!/usr/bin/python3
# encoding: utf-8

import pandas as pd
import numpy as np

if __name__ == "__main__":
    reader = pd.read_csv(
        "C:/Users/ROBO-E-03/Desktop/scope/data/clasification/" \
        "classification_5.12.txt",
        header=None)

    offset = 0

    result = []
    for index, row in reader.iterrows():
        start = row[0] * 60 + row[1] - offset
        end = row[2] * 60 + row[3] - offset
        state = row[4]

        for t in range(start, end):
            result.append([t, state])

    writer = pd.DataFrame(result, columns=['time', 'state'])
    print(writer)
    writer.to_csv(
        "C:/Users/ROBO-E-03/Desktop/scope/data/clasification/" \
        "classify_per_sec_5.12.csv")