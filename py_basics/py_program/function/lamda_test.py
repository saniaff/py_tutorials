#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
author= "towan"
mtime= "16-4-23"
"""

square = [x**2 for x in range(4)]
print square

def add(x,y):
    return x+y
print add(2,3)

c = lambda x,y:x+y
print c(2,3)

seq = [0 for _ in range(4)]
print seq