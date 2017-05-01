#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= "文件读取的测试，按批读取"
ctime = 2016/08/31
"""

def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            # print("block",block)
            if block:
                yield block
            else:
                return