#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= "测试函数的传递"
author= "towan"
mtime= "16-4-23"
"""
def convert(func,seq):
    return [func(ele) for ele in seq]

seq = [1,2,3,4,6,-0.5,999L]

print convert(int,seq)
print convert(float,seq)