#!/usr/bin/python3
# encoding: utf-8

import pandas as pd
import numpy as np

if __name__ == "__main__":
    sensor_csv = pd.read_csv(
        'C:/Users/ROBO-E-03/Desktop/scope/data/sensor_per_sec.csv',
        index_col=0)
    classify_csv = pd.read_csv(
        'C:/Users/ROBO-E-03/Desktop/scope/data/clasification/' \
        'classify_per_sec_5pos.6.csv',
        index_col=0)

    records = []
    for index, row in classify_csv.iterrows():
        t = row['time']
        s = row['state']
        acc = sensor_csv.get_value(t, 'acc')
        ch1 = sensor_csv.get_value(t, 'ch1')
        ch2 = sensor_csv.get_value(t, 'ch2')
        ch3 = sensor_csv.get_value(t, 'ch3')
        ch4 = sensor_csv.get_value(t, 'ch4')
        ch5 = sensor_csv.get_value(t, 'ch5')
        ch6 = sensor_csv.get_value(t, 'ch6')

        # rec = [t, s, acc, ch1, ch2, ch3, ch4, ch5]
        rec = [t, s, acc, ch1, ch2, ch3, ch4, ch5, ch6]
        records.append(rec)

    sample = pd.DataFrame(records)
    # sample.columns = ['time', 'state', 'acc',
      #                'ch1', 'ch2', 'ch3', 'ch4', 'ch5']
    sample.columns = ['time', 'state', 'acc',
                      'ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6']

    sample.to_csv('C:/Users/ROBO-E-03/Desktop/scope/data/sample.csv')


