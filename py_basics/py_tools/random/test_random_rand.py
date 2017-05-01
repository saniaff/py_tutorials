#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
author= "towan"
mtime= "16-4-23"
"""
from numpy import  random

embedding_dim  = 5
w2v = random.rand(1, embedding_dim)[0] #这里是两层 (5,)
print w2v
print type(w2v)
print  w2v.shape
w2v2 = random.rand(1, embedding_dim)
print w2v2
print type(w2v2)
print w2v2.shape (1,5)