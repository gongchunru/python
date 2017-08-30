#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/17 11:14
# @Author  : gongchunru
# @Site    : 
# @File    : test_connection.py
# @Software: PyCharm

import MySQLdb

conn = MySQLdb.Connect(host = '127.0.0.1',
                       port = 3306,
                       user = 'root',
                       passwd = '123456',
                       db = 'test',
                       charset = 'utf8')

cursor = conn.cursor()

print conn
print cursor

cursor.close()
conn.close()
