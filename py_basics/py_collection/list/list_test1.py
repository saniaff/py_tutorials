#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
author= "towan"
mtime= "16-4-23"
"""

list = [1,2,3,4,5,6]
print list[:3]
list[2] = 100

print list[:3]

tuple = {1,2,3,4,5,6}
print tuple
tuple[2] = 123 #元组不可以修改