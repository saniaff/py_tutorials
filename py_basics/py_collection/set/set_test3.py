#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= "大括号创建集合对象,不能加入集合，元素的类型可以不一致"
author= "huangtw"
ctime = 2017/04/30
"""
s = {1,2,1,2}
print s

# 添加多个
s.update({3,4})
print s

# 添加一个
s.add(7)
print s

s.add('abc')
print s