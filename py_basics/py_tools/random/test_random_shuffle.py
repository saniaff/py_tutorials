#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
ctime = 2016/09/07
"""
import numpy as np
np.random.seed(111)

def shuffle_array_by_size(array_src,rand_size):
    array_x = range(len(array_src))
    print("array_src", array_src)
    np.random.shuffle(array_x)
    print("array_x", array_x)

    # 构建一个打乱后的0索引下标到其数值的映射
    new_index_value_map = {}
    for i in range(rand_size):
        new_index_value_map[i] = array_x[i]
    # print("new_index_value_map", new_index_value_map)

    # 构建一个打散的小标索引map
    arg_index = np.array(array_x[:rand_size]).argsort()  # argsort函数返回的是数组值从小到大的索引值
    # print("arg_index", arg_index)
    old_index_value_map = {}
    for i in range(rand_size):
        old_index_value_map[i] = array_x[arg_index[i]]
    # print("old_index_value_map", old_index_value_map)

    # 开始数值替换原有的array
    for i in range(rand_size):
        array_src[old_index_value_map[i]] = new_index_value_map[i]#数值要存在 TODO
    # print("array_src", array_src)
    return array_src


def shuffle_array_by_size2(array_src,rand_size):

    #下标位置打散
    array_x = range(len(array_src))
    print("array_src", array_src)
    np.random.shuffle(array_x)
    print("array_x", array_x)

    #建立新老索引的map，新索引为key,老位置为value,小对小 TODO
    index_map = {}
    arg_index = np.array(array_x[:rand_size]).argsort()
    for i in range(rand_size):
        index_map[i] = arg_index[i]

    #建立原始的下标到值的映射
    src_index_value_map = {}
    for i in range(rand_size):
        src_index_value_map[array_x[i]] = array_src[array_x[i]]

    for i in range(rand_size):
        array_src[index_map[i]] = src_index_value_map  #TODO

    return array_src

# size = 15
# array_src = range(size)
array_src = [19,22,1,8,9,2,5,2,3,1]
rand_size = 4

shuffle_array = shuffle_array_by_size(array_src,rand_size)
print("shuffle_array",shuffle_array)



# ('array_src', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) 不管原数组是否重复
# ('array_y', [11, 7, 5, 9])
# ('array_index', [3, 1, 0, 2])
# ('arg_sort_index', array([2, 1, 3, 0]))