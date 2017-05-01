#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
ctime = 2016/09/08
"""
import copy

x = [22, 1, 5, 6, 3, 1, 2, 9, 5, 2]
x2 = copy.deepcopy(x)
print("x2",x2)
x3 = copy.copy(x)
print("x3",x3)

x[2] = 100
print("x",x)
print("x2",x2)
print("x3",x3)

print("x",x)
print("x2",x2)
print("x3",x3)