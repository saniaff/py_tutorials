#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
ctime = 2016/10/27
"""

from collections import deque

q = deque(range(5))

q.append(3)
q.appendleft(99)
print(q)

print q.popleft()

print q
q.rotate(3)
print q