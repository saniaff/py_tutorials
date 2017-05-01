#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= "生成器和普通方法"
author= "huangtw"
ctime = 2017/01/13
"""

def gensquares(N):
    """
    返回一个列表
    :param N:
    :return:
    """
    res = []
    for i in range(N):
        res.append(i*i)
    return res

for item in gensquares(5):
    print item,


print('\n')
def gensquares(N):
    for i in range(N):
        yield i*i

for item in gensquares(5):
    print item,