#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
ctime = 2016/11/10
"""

a = '     123'
b = a.strip()
print("b",b)

a = '\t\tanc'
b = a.strip()
print("b",b)

a = '\t\tanc\n'
b = a.strip()
print("b",b)


a = '123abc'
b = a.strip('21')
print("b",b)

a = '123abc'
b = a.strip('12')
print("b",b)