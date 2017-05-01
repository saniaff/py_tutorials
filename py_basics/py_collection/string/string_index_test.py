#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
title= "内置方法index的测试"
ctime = 2016/11/10
"""

str1 = "this is string example....wow!!!";
str2 = "exam"

print str1.index(str2)
print str1.index(str2, 10)
try:
    print str1.index(str2, 40)
except Exception, m:
    print("tabke fail", m.message)
