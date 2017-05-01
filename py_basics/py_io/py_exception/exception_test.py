#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= "异常测试"
"""

a = 1.0
b = 0
try:
    c= a/b
    print "c", c
except ZeroDivisionError:
    print ZeroDivisionError.message,ZeroDivisionError.args