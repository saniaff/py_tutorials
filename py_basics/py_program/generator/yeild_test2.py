#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= "
yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，
Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，
而是返回一个 iterable 对象！"
ctime = 2016/08/31
"""

def fib(max):
    n = 0
    a = 0
    b = 1

    while n < max:
        print b
        tmp = a
        a = b
        b = tmp+b
        n = n+1

def fib2(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L

fib(5)
print("*" * 100)

print(fib2(5))


class Fab(object):
    """
     fab 函数改写为一个支持 iterable 的 class
    """

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

print("*"*100)

for n in Fab(5):
    print("num",n)

print("*"*100)

def fab4(max):
    """
    yeild版本的fib处理
    把 print b 改为了 yield b，就在保持简洁性的同时获得了 iterable 的效果
    :param max:
    :return:
    """
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1


g = fab4(5) #测试带yeild的生成器函数
print "next", g.next()
print "next", g.next()
print "next", g.next()

# 判断一个函数是否是一个特殊的 generator 函数
from inspect import isgeneratorfunction
print isgeneratorfunction(fab4)

# 类的定义和类的实例
import types
print isinstance(fab4, types.GeneratorType)
print isinstance(fab4(5), types.GeneratorType)