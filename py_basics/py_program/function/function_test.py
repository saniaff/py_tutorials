#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
author= "towan"
mtime= "16-4-23"
"""

def addMe(x):
    'add twice'
    return  x+x

src = 3
a = addMe(src)
print "%s,now invoke addme is %s" %(src,a)

src = "hello"
a = addMe(src)
print "%s,now invoke addme is %s" %(src,a)