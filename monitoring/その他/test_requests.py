#!/usr/bin/python3
# encoding: utf-8

import requests

path = 'http://sansa.cs.shinshu-u.ac.jp/akita/MMRK/live.php'
mamoru_id = '2001'
ver = '1'
boot = '1'
post_path = path + "?ID=" + mamoru_id + "&VER=" + ver + "&BOOT=" + boot
payload = {'ID': '2001', 'VER': '1', 'BOOT': '1', 'BED': 'blue', 'PIL': 'yellow'}

r = requests.post(post_path, params=payload)
print(r.text)

