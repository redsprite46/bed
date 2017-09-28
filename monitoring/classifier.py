#!/usr/bin/python3
# encoding: utf-8

import numpy as np
import redis
from sklearn.externals import joblib


class Classifier:
    def __init__(self):
        self.redis_ = redis.Redis(host='192.168.60.1', port=6379)
        # self.acc_ = np.zeros(3, dtype=np.float)
        self.piezo_ = np.zeros(5, dtype=np.float)
        self.classifier_ = joblib.load('/home/ub/scope/data/cls_murosawa.pkl')
        self.redis_.set('prediction', 'g')
        self.leave_triggered_ = False
        self.moving_counter_ = 0

    def update_latest_values(self):
        piezo_len = self.redis_.llen('judge_piezo')
        if piezo_len >= 10:
            self.piezo_ = np.zeros(5, dtype=np.float)

            data_array = self.redis_.lrange('judge_piezo', 0, 10)

            prev = np.zeros(5, dtype=np.float)
            for data in data_array:
                if data is None:
                    next
                data = data.decode('utf-8').split(':')
                for i in range(5):
                    val = int(data[3 + i])
                    val = val / 1023.0 * 10 - 5.0
                    self.piezo_[i] += abs(prev[i] - val)
                    prev[i] = val

    def classify(self):
        self.update_latest_values()
        print((self.piezo_))

        prev = self.redis_.get('prediction')
        if prev:
            prev = prev.decode('utf-8')
        else:
            prev = 'g'
        pred = prev

        if max(self.piezo_[0], self.piezo_[1]) > 0.15:
            pred = 'a'
        elif max(self.piezo_[2], self.piezo_[3]) > 0.15:
            self.moving_counter_ += 1
            if self.moving_counter_ > 2:
                pred = 'd'
        elif self.piezo_[4] > 0.3:
            self.leave_triggered_ = True
            pred = 'd'
        else:
            if self.leave_triggered_:
                pred = 'g'
                self.leave_triggered_ = False

        self.redis_.set('prediction', pred)

        # pred = self.classifier_.predict([self.piezo_])
        # print(pred[0])
        # self.redis_.set('prediction', pred[0])

    def reset(self):
        print("classifier reset")
        self.leave_triggered_ = False
        self.moving_counter_ = 0
