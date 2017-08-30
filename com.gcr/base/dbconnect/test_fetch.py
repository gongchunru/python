#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/18 11:38
# @Author  : gongchunru
# @Site    : 
# @File    : test_fetch.py
# @Software: PyCharm

import MySQLdb

conn = MySQLdb.Connect(host = '127.0.0.1',
                       port = 3306,
                       user = 'root',
                       passwd = '123456',
                       db = 'test',
                       charset = 'utf8')

cursor = conn.cursor()

sql = "select * from user  "

cursor.execute(sql)

rs = cursor.fetchone()
print rs
rs = cursor.fetchall()
print rs



# -----测试 遍历

cursor.execute(sql)
res = cursor.fetchall()
for row in res:
    print "id=%s, name=%s, pwd=%s, create=%s" % row



cursor.close()
conn.close()