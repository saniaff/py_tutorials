#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
ctime = 2016/11/10
"""

import time
import sys

for i in range(5):
    print i,
    # sys.stdout.flush() 保证及时输出
    time.sleep(1)