#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
mtime= "16-5-20"
"""

import random
from numpy import array

list = [20, 16, 10, 5];
random.shuffle(list)
print "随机排序列表 : ",  list

random.shuffle(list)
print "随机排序列表 : ",  list

aa = range(100)
print aa
random.shuffle(aa)
print aa

cc = range(5)
random.shuffle(cc)

aa = range(40)
aa = array(aa)
print aa
bb = aa.reshape(5,4,2)
print bb
print("cc",cc)
dd = bb[cc]
print("dd",dd)

