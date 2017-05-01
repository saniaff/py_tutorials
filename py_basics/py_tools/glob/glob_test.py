#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= "正则文件查找"
author= "huangtw"
ctime = 2017/03/15
"""

import glob

#父目录中的.py文件
f = glob.iglob(r'*.py')

print("glob", f) #<generator object iglob at 0x00B9FF80>

for py in f:
    print("filename", py)