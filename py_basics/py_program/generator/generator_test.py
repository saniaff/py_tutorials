#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
author= "huangtw"
ctime = 2017/01/12
"""
def spam():
    yield"first"
    yield"second"
    yield"third"

for x in spam():
    print x

print('*'*100)
gen = spam()
print gen.next()
print gen.next()
print next(gen)
