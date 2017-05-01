#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= "中文输出的测试(fail)-着了print()是作为元组进行输出"
author= "huangtw"
ctime = 2017/04/29
"""

l = ["a", "b"]
# 汉字和列表的输入
print("私有变量".decode('utf-8'), l)

print(u"私有变量", l)
print(r"私有变量", l)
print("私有变量", l)
print("私有变量".decode('utf-8'), "".join(l))
print "私有变量", l