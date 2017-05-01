#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
mtime= "16-5-14"
"""

line = " A B C D E F G H"
print("input=",line)
print("input=",line[1:])

revLine = line[::-1]
print("revLine=",revLine)
print("revLine=",revLine[1:])
print("revLine=",revLine[::-1][1:])


enLine = ",A,Bes,C,Des,E"
list_from_line = enLine.split(",")
print list_from_line
list_from_line = list_from_line[::-1][:-1]
print list_from_line
print("after",list_from_line)
enLine = ",".join(list_from_line)
print enLine