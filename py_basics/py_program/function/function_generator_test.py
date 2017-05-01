#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
author= "towan"
mtime= "16-4-23"
"""
def gen():
    yield 1
    yield '2-->punsh'

m = gen()

print m.next()
print m.next()
# print m.next() # error

