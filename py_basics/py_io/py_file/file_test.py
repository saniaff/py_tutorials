#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
ctime = 2016/12/11
"""
import numpy as np

fr = open('./test.txt', 'r')

# for i in range(4):
#     line = "3"
#     for j in range(10):
#         b = np.random.randint(20)
#         line = "%s%s%s"%(line,'\t',b)
#     print("line", line)
#     fr.write("%s%s%s"%(line, '\t','\n'))

# for line in fr.readlines():
#     print(line)
#
# fr.seek(0, 0)
# for line in fr.readlines():
#     print("line",line.strip())

def get(s,ts):
    for t in ts:
        s = s.replace(t,'')
    print s

# positive_examples = list(open("./test.txt").readlines())
# ts = "3"
# positive_examples = [get(s,ts)for s in positive_examples]

from pprint import pprint
# pprint(positive_examples)

list = []
list.append("abc")
list.append("def")
pprint(list)
# [[vocabulary[word] for word in sentence] for sentence in sentences]
l2 = [[s for s in line]for line in list]
pprint(l2)
# ts = "abc"
# for i in ts:
#     print("cur-line",i)