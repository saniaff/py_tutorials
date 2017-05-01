#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= "默认的函数参数"
author= "towan"
mtime= "16-4-23"
"""
def tax(cost, rate=0.2):
    return cost*(1+rate)

def tupleVarParam(arg1,arg2='default',*theRest):
    print 'format arg 1',arg1
    print 'format arg 2',arg2
    for ele in theRest:
        print('rest param:',ele)

def dicVarParam(arg1,arg2='default',**theRest):
    print 'format arg 1',arg1
    print 'format arg 2',arg2
    for ele in theRest.keys():
        print('rest param:',ele,theRest.get(ele))

print tax(1)
print tax(1,0.3)

tupleVarParam('abc')
tupleVarParam('abc','12')
tupleVarParam('abc','1','2')


dicVarParam(1)
dicVarParam(1,2)
dicVarParam(1,2,d="11",e='22')