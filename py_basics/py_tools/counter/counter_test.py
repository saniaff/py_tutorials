#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
author= "huangtw"
ctime = 2017/01/13
"""

from collections import Counter

c = Counter('gallahad')  # 从一个可iterable对象（list、tuple、dict、字符串等）创建
print("counter", c)
for ii, cc in enumerate(c.most_common()):
    print("index", ii, "char", cc)

c.update('switch')
print(c)

c.update('gallahad')
print(c)

c.subtract('switch')
print(c)

c.subtract('switch') # 计数可以为负数
print(c)
