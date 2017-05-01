#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
mtime= "16-7-16"
"""
import time

# time.time() 获取当前时间戳
# time.localtime() 当前时间的struct_time形式
# time.ctime() 当前时间的字符串形式
t = time.clock()
print("t",t)
s = time.time()
print("s",s)

t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("time",t)

#休眠秒数
time.sleep(1)
c = time.clock()
print("c", c)