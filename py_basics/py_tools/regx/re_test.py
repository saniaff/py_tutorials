#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
ctime = 2016/11/10
"""

import re
p = re.compile('(one|two|three)')

# 替换num的个数
print p.sub('num','one word two words three words apple', 2)


_DIGIT_RE = re.compile(br"\d")
x = re.sub(_DIGIT_RE, b"0", "12368")
print("x",x) #  数字替换为0



tokens = "c" if "A" else "V"
print("tokens",tokens)

tokens = "c"*10 if "" else "V"
print("tokens",tokens) #V

tokens = "" if "CC" else "V"
print("tokens",tokens) #V

tokens = "5" if 5<3 else 10
print("tokens",tokens) #V