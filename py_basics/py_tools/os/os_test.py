#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
author= "towan"
mtime= "16-4-23"
"""
import os
cwd = os.getcwd()
print "cwd",cwd #当前目录
files = os.listdir(cwd)
print files #目录下的文件
print "len:",len(files)