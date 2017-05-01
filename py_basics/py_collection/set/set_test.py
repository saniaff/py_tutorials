#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
author= "towan"
mtime= "16-4-23"
"""

s1 = set([1,3,5])
s2 = set([3,5,8])

print s1&s2 #交集
print s1
print s2

print s1|s2 #并集
print s1
print s2

print s1-s2 #差集
print s1
print s2

print s1^s2 #异或
print s1
print s2

s1.add(7)
print "len",len(s1)