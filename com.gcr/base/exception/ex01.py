#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/15 00:09
# @Author  : gongchunru
# @Site    : 
# @File    : ex01.py
# @Software: PyCharm

try:
    f = open("2.txt")
    print int(f.read())
finally:
    print "file close"
    f.close()
