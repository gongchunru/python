#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/30 23:38
# @Author  : gongchunru
# @Site    : 
# @File    : testWith.py
# @Software: PyCharm


class Sample:
    def __enter__(self):
        print "In __enter__()"
        return "Foo"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print "In __exit__"


def get_sample():
    return Sample()


with get_sample() as sample:

    print "sample:",sample