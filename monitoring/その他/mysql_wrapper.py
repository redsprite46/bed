#!/usr/bin/python3
# encoding: utf-8

import pymysql.cursors


class MySQLWrapper:

    def __init__(self):
        self.connection_ = pymysql.connect(
            host='localhost',
            user='dbuser',
            password='dbpass',
            port=3307,
            db='mamoru',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)
        self.connection_.autocommit(True)

    def query_mamoru_enabled(self):
        mamoru_enabled = None
        with self.connection_.cursor() as cursor:
            query = "select SQL_NO_CACHE * from mamorulog where id ="
            query += " (select max(id) from mamorulog"
            query += " where eventname='KEY' or eventname='SW1'"
            query += " or eventname='SW2')"
            cursor.execute(query)

            results = cursor.fetchall()
            # import pprint
            # pp = pprint.PrettyPrinter(indent=4)
            # pp.pprint(results)
            result = results[0]
            if result['eventname'] == 'KEY':
                mamoru_enabled = (result['postedval'] == 'ON')
            elif result['eventname'] == 'SW1':
                # absence
                mamoru_enabled = False
            elif result['eventname'] == 'SW2':
                # home
                mamoru_enabled = True
        return mamoru_enabled

    def close(self):
        self.connection_.close()

if __name__ == '__main__':
    mysql_wrapper = MySQLWrapper()
    b = mysql_wrapper.query_mamoru_enabled()
    print(b)
    mysql_wrapper.close()
