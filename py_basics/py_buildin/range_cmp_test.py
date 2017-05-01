#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
author= "huangtw"
ctime = 2017/01/13
"""

import time
# t = time.time()
# a = sum([i for i in xrange(10000000000)]) #内存消耗,Process finished with exit code 137
end = time.time()
# print("using time:%s"%(end-t))
b = sum(i for i in xrange(10000000000)) # 是个生成器
end2 = time.time()
print("using time:%s"%(end2-end))