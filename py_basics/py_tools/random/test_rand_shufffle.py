#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= "测试打乱数组的顺序"
ctime = 2016/09/08
"""
import numpy as np
import  copy

np.random.seed(1337)

def get_index_map(index_list):
    '''
    :param index_list:
    :return:
    '''
    arr = np.array(index_list)
    arr_index = np.argsort(arr)  # 2,1,3,0
    index_dic = {}
    for i in range(len(arr)):
        index_dic[index_list[i]] = index_list[arr_index[i]]
    # print("index_dic", index_dic)
    return index_dic


def get_random_list(x,rnd_size):
    x2 = copy.copy(x)
    # print("x2",x2)
    index = range(len(x))
    np.random.shuffle(index)
    index_list = index[:rnd_size]
    print("index_list",index_list,"index",index)
    index_map = get_index_map(index_list)
    #使用index_list[6, 3, 0, 4] 进行替换x数组[5, 3, 0, 4, 1, 2, 6, 9, 8, 7]
    #目前的做法是:
    # 1.index_list的下标得到实际对应的值为[x1,x2,x3,x4]
    # 2.循环开始遍历 index_list:
    #  2-1 i=0时，index_list[i]的值是位置6，位置6的值要去替换位置最小的0位置的 x[6]=x[0]
    #  2-1 i=1时，index_list[i]的值是位置3，位置3的值要去替换位置最小的0位置的 x[3]=x[3]
    #  2-1 i=2时，index_list[i]的值是位置0，位置0的值要去替换位置最小的0位置的 x[0]=x[4]
    #  2-1 i=3时，index_list[i]的值是位置4，位置4的值要去替换位置最小的0位置的 x[4]=x[6]
    #实质就是建立这个映射

    # print("before-x:",x2)
    for i in index_list:
        x2[i] = x[index_map[i]]
    # print("after-x",x2)
    return x2

# x = [22, 1, 5, 6, 3, 1, 2, 9, 5, 2]
# rnd_size = 4
# rand_arr = get_random_list(x,rnd_size)
# print("rand_arr",rand_arr)
#
# print("*"*100)

x = range(10)
y = range(10)
rnd_size = 4
rand_arr = get_random_list(x,rnd_size)
rand_arr_y = get_random_list(y,rnd_size)
print("rand_arr",rand_arr)
print("rand_arr_y",rand_arr_y)