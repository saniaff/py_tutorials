#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
author= "towan"
mtime= "16-4-23"
"""
def foo():
    def bar():
        print "bar called"
    print "foo call"
    bar()


foo()
# foo().bar()