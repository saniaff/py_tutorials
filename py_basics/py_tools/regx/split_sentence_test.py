#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
ctime = 2016/11/10
"""

import re
# Regular expressions used to tokenize.
_WORD_SPLIT = re.compile(b"([.,!?\"':;)(])")

def basic_tokenizer(sentence):
  """Very basic tokenizer: split the sentence into a list of tokens."""
  words = []
  for space_separated_fragment in sentence.strip().split():
    print("space_separated_fragment",space_separated_fragment)
    #进一步划分列表
    split = re.split(_WORD_SPLIT, space_separated_fragment)
    print("space_separated_fragment2",split)
    words.extend(split)
  return [w for w in words if w]

sentence = 'hew:l[lo world'
result = basic_tokenizer(sentence)
print("result",result)