#!/usr/bin/python3
# encoding: utf-8

import pandas as pd
import numpy as np
import math

if __name__ == '__main__':
    sensor_csv = pd.read_csv(
        'C:/Users/ROBO-E-03/Desktop/scope/data/sensor.csv')

    records = []

    record = np.zeros(7)
    pre = {}
    for index, row in sensor_csv.iterrows():
        if index % 50 == 49:
            records.append(record)
            record = np.zeros(7)
        if index % 5 == 0:
            x = sensor_csv.get_value(index, 'acc_x')
            y = sensor_csv.get_value(index, 'acc_y')
            z = sensor_csv.get_value(index, 'acc_z')

            ch1 = sensor_csv.get_value(index, 'ch1')
            ch2 = sensor_csv.get_value(index, 'ch2')
            ch3 = sensor_csv.get_value(index, 'ch3')
            ch4 = sensor_csv.get_value(index, 'ch4')
            ch5 = sensor_csv.get_value(index, 'ch5')
            ch6 = sensor_csv.get_value(index, 'ch6')

            dx = 0.0
            dy = 0.0
            dz = 0.0

            d1 = 0.0
            d2 = 0.0
            d3 = 0.0
            d4 = 0.0
            d5 = 0.0
            d6 = 0.0

            if 'x' in pre:
                dx = x - pre['x']
            if 'y' in pre:
                dy = y - pre['y']
            if 'z' in pre:
                dz = z - pre['z']
            if 'ch1' in pre:
                d1 = ch1 - pre['ch1']
            if 'ch2' in pre:
                d2 = ch2 - pre['ch2']
            if 'ch3' in pre:
                d3 = ch3 - pre['ch3']
            if 'ch4' in pre:
                d4 = ch4 - pre['ch4']
            if 'ch5' in pre:
                d5 = ch5 - pre['ch5']
            if 'ch6' in pre:
                d6 = ch6 - pre['ch6']

            record[0] += math.sqrt(dx * dx + dy * dy + dz * dz)
            record[1] += abs(d1)
            record[2] += abs(d2)
            record[3] += abs(d3)
            record[4] += abs(d4)
            record[5] += abs(d5)
            record[6] += abs(d6)

            pre['x'] = x
            pre['y'] = y
            pre['z'] = z
            pre['ch1'] = ch1
            pre['ch2'] = ch2
            pre['ch3'] = ch3
            pre['ch4'] = ch4
            pre['ch5'] = ch5
            pre['ch6'] = ch6

    print(records)
    sensor_per_sec = pd.DataFrame(records)
    print(sensor_per_sec)
    sensor_per_sec.columns = ['acc', 'ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6']
    sensor_per_sec.to_csv(
        'C:/Users/ROBO-E-03/Desktop/scope/data/sensor_per_sec.csv')
