#!/usr/bin/python3
# encoding: utf-8

import pandas as pd
import numpy as np

if __name__ == "__main__":
    sensor_columns = ['acc_x', 'acc_y', 'acc_z',
                      'ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6']

    bed_csv = pd.read_csv("C:/Users/ROBO-E-03/Desktop/scope/data/bed2.csv",
                          header=None, skiprows=[0, 1])
    bed_csv.columns = sensor_columns

    pillow_csv = pd.read_csv(
        "C:/Users/ROBO-E-03/Desktop/scope/data/pillow1.csv",
        header=None, skiprows=[0, 1])
    pillow_csv.columns = sensor_columns

    record_len = min(len(bed_csv), len(pillow_csv))

    records = []
    for i in range(record_len):
        records.append([pillow_csv.get_value(i, 'acc_x'),
        pillow_csv.get_value(i, 'acc_y'),
        pillow_csv.get_value(i, 'acc_z'),
        bed_csv.get_value(i, 'ch1'),
        bed_csv.get_value(i, 'ch2'),
        bed_csv.get_value(i, 'ch3'),
        bed_csv.get_value(i, 'ch4'),
        bed_csv.get_value(i, 'ch5'),
        bed_csv.get_value(i, 'ch6')])

    sensor_csv = pd.DataFrame(records)
    sensor_csv.columns = sensor_columns
    sensor_csv.index = \
        [(i // 50) + (i % 50) * 0.02 for i in range(record_len)]

    sensor_csv.to_csv('C:/Users/ROBO-E-03/Desktop/scope/data/sensor.csv')
