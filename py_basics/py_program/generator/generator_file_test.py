#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= "生成器只遍历一次,没有结果"
author= "huangtw"
ctime = 2017/01/13
"""

def get_province_population(filename):
    with open(filename) as f:
        for line in f:
            yield int(line)

gen = get_province_population('data.txt')
all_population = sum(gen)
print("all_population",all_population) #求出总数
#print all_population
for population in gen:
    print population / all_population

#处理有五个方法,先使用重新创建的方式.后面使用send的方式

gen2 = get_province_population('data.txt')
#print all_population
for population in gen2:
    print('%.10f'%(population/float(all_population))) # 分母是float即可

