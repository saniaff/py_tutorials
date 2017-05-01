#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
ctime = 2016/11/10
"""
vocab = {}
vocab[12]= 15
vocab[122]= 125
vocab[2]= 1533
print(vocab)
vo = sorted(vocab, key=vocab.get, reverse=True)
print(vo)