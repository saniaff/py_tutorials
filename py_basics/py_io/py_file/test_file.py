#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
author= "towan"
mtime= "16-4-23"
"""
import os

fobj = open("test",'r')

for line in fobj:
    print line, #这里需要一个逗号，否则中间多空一行？以免输出\n
fobj.close()

line = "aaa"
filename = 'data.txt'
fr= open(filename, 'a')
fr.write("\n"+line)
fr.close()

if os.path.isfile(filename):
 os.remove(filename)

fr= open(filename, 'a')
iter = 3
curTime = 5
hist = [23,4,4,5,6]
fr.write('Iter={0},curTime={1},hist={2}{3}'.format(iter,curTime,hist,'\n'))
fr.write('Iter={0},curTime={1},hist={2}{3}'.format(iter,curTime,hist,'\n'))
fr.write('Iter={0},curTime={1},hist={2}{3}'.format("33",curTime,hist,'\n'))