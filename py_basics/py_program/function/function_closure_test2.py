#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
author= "towan"
mtime= "16-4-23"
"""
def counter(start_at=0):
    count = [start_at] #接受一个初始值
    def incr():##一个内部函数用与递增
        count[0]+=1
        return count[0]
    return incr#返回一个初始inc对象

count = counter(5)
print count()
print count()

count = counter(105)
print count()
print count()