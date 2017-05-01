#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= "测试any or all表达式"
ctime = 2016/10/16
"""

print any('123') # True
print any([0, 1])# True
print any([0, ''])# False
print all('123')# True

print all([0, 1])# False
print all([1, 2])# True
