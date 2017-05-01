#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
mtime= "16-5-19"
"""

from numpy import random
random.seed(1337)
xx = random.uniform(-0.025,0.025,10)
print(xx)

ss = range(20)
print ss
random.shuffle(ss)
print ss

