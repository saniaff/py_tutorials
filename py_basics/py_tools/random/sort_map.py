#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
ctime = 2016/09/08
"""
import numpy as np

def get_index_map(list):
    arr = np.array(list)
    ##映射到0,3,4,6
    index = np.argsort(arr)  # 2,1,3,0
    print(index)  # 0,3,4
    index_dic = {}
    for i in range(len(arr)):
        index_dic[list[i]] = list[index[i]]
    print("index_dic", index_dic)
    return index_dic


list = [6, 3, 0, 4]
m = get_index_map(list)

for k,v in m.items():
    print(k,"--->",v)
