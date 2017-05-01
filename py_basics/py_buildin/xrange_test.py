#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= "xrange采用的迭代操作，更加高效"
author= "towan"
mtime= "16-4-23"
"""
# xrange节省内存
for i in xrange(6):
    print i


t = xrange(6)
print("t",t)
print("t",t[0])
print("t",t[5])
print("t",t[4])