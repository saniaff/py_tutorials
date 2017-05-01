#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
ctime = 2016/07/19
"""

line = "aa bb cc dd ee ff aa bb"
sents = line.split(' ')
s1 = set(sents)
print("sents",sents,"s1",s1)

line2 = "aa bb gg kk ff aa bb"
sents2 = line2.split(' ')
s2 = set(sents2)
print("sents",sents2,"s2",s2)

s1 = s1.union(s2)
print("s1",s1,"s2",s2)
print("type-s1",type(s1),"type-sent",type(sents))


# s1 = ('a','b','c')
# s2 = ('a','b','c')
# s3 = ('d','b','c','f')
#
# s = (s1,s2,s3)
# print("doc-type",s.shape,"content",s)
# doc = ()
# doc[0] = s
#
# print("doc-type",doc.shape,"content",doc)

word_idx_map = dict()##有序吗
word_idx_map["a"] = "cc"
word_idx_map["b"] = "dcc"
word_idx_map["c"] = "efcc"


print("status",word_idx_map)
if  word_idx_map.has_key("a"):
    print("true")
else:
    print("false")

s = set()
s.add("abc")
s.add("bc")
s.add("abc")
print(s)
