#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= "
Python使用生成器对延迟操作提供了支持。所谓延迟操作，是指在需要的时候才产生结果，而不是立即产生结果。这也是生成器的主要好处。
Python有两种不同的方式提供生成器：
    生成器函数：常规函数定义，但是，使用yield语句而不是return语句返回结果。yield语句一次返回一个结果，
    在每个结果中间，挂起函数的状态，以便下次重它离开的地方继续执行
    生成器表达式：类似于列表推导，但是，生成器返回按需产生结果的一个对象，而不是一次构建一个结果列表
"
author= "huangtw"
ctime = 2017/01/12
"""
l = [x*4 for x in 'abcd'] #一次就运行完
print("list", l)

# 这里是生成器
G = (c*4 for c in 'abcd')
# print list(G)
print next(G)
print next(G)
print next(G)
print next(G)