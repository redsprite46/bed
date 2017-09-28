#!/usr/bin/python3
# encoding: utf-8

import redis

rd = redis.Redis(host='192.168.60.3', port=6379)

while True:
    data_len = rd.llen('monitor_acc')
    if data_len > 0:
        for i in range(data_len):
            s = rd.lpop('monitor_acc')
            ss = s.decode('utf-8').split(':')
            print(ss[5])
