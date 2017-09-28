#!/usr/bin/python3
# encoding: utf-8

import pymysql.cursors
import pprint


if __name__ == '__main__':
    connection = pymysql.connect(
        host='localhost',
        user='dbuser',
        password='dbpass',
        port=3307,
        db='mamoru',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        sql = 'select * from mamorulog where mamoruid=2001 group by eventname'
        cursor.execute(sql)

        results = cursor.fetchall()
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(results)

    connection.close()
