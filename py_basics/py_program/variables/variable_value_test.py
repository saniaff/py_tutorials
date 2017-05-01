#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= "测试变量复制"
author= "towan"
mtime= "16-4-23"
"""

#增量赋值
x = 1
x += 1
print x

#多重赋值
x = y= z=1
print x, y, z

#多元赋值
x, y, z = 1, 100, 'aa'
print x, y, z