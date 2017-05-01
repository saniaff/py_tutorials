#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= "异常的处理和捕获"
ctime = 2016/08/24
"""

a = 1
b = 2
print a / b

b = 0

try:
    c = a / b
    print("c", c)

except ZeroDivisionError, Argument:
    # except Exception:
    print("cal error")
    print("cal error", Argument) #异常输出参数
finally:
    print("over!!!!")

for i in range(5):
    print("index", i)


