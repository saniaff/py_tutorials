#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
author= "towan"
mtime= "16-4-23"
"""
def func(n):
    if n==0 or n==1:
        return 1
    else:
        return n*func(n-1)


x = func(10)
print(x)
print(func(5))