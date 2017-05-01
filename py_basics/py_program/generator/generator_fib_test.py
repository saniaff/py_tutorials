#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= "yield就是专门给生成器用的return(加上点小魔法)"
author= "huangtw"
ctime = 2017/01/12
"""
def fib():
    first, second=0, 1
    while True:
        yield second
        first, second = second, first+second

print(next(fib()))
print(next(fib()))
print(next(fib()))