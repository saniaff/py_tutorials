#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
author= "towan"
mtime= "16-4-23"
"""

map = {"ip":'local', "port":8080} #这样的map是否乱序
print map

for key in map.keys():
    print key, map.get(key)

print map.items()
print map.values()