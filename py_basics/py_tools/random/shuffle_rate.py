#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
ctime = 2016/09/07
"""

import numpy as np

rnd = np.random
rnd.seed(113)

size = (4, 10)

a = rnd.randint(5, size=size)
print(a)

a = rnd.randint(5, size=size)
print(a)
a.shape


def rand_rate(x,rnd_num):
    '''
    随机化数组的个数
    :param x:
    :param rnd_num:
    :return:
    '''
    pass


def get_rate_arr(arr,rnd_rate):
    shape = a.shape
    arr_len = shape[1]
    #随机的个数
    rnd_num = int(arr_len*rnd_rate)
    arr = [rand_rate(x,rnd_num) for x in arr]
    return arr

def shuffle(arr):
    '''
    shuffle函数比例
    :param arr:
    :return:
    '''
    arr_len = len(arr)
    for i in xrange(arr_len):
        index = np.random.randint(0,arr_len)
        tmp = arr[index]
        arr[index] = arr[i]
        arr[i] = tmp
    return arr

def shuffle_rate(arr,rate=1):

    rand_size = int(len(arr)*rate)

    index_arr = range(len(arr))
    np.random.shuffle(index_arr)
    #下表位置索引
    brr = range(rand_size)
    crr = shuffle(brr)
    #使用crr进行选择index_arr

# size = (4, 10)
# a = rnd.randint(5, size=size)
# print(a)
arr = range(100)
np.random.shuffle(arr)
print("array",arr)
barr = shuffle(arr)

print("array",arr)
print("array",barr)

barr = shuffle(arr)
print("array",arr)
print("array",barr)

barr = shuffle(arr)
print("array",arr)
print("array",barr)