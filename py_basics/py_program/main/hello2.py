#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
ctime = 2016/10/27
"""
import hello

def hello():
    print "this hello2"

print "hello name", hello.__name__
print(__name__)

if __name__=='__main__':
    hello()


import copy
print(dir(copy))