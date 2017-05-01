#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= "求集合的交集"
ctime = 2016/09/06
"""

la =['a','b','c']
lb = ['cc','dd','c']

la = set(la)
lb = set(lb)

c = la & lb# 交集
# c = la^lb
print(c)