#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
title= "关机脚本"
ctime = 2016/12/11
"""

import sys
import os
import time

reload(sys)
sys.setdefaultencoding("UTF-8")

# shutdown computer after time_diff seconds
def shutdown(seconds):
    print str(seconds) + u' 秒后将会关机...'
    time.sleep(seconds)
    print u'关机啦。。。'
    os.system('shutdown -s -f -t 1')

def ls_dir():
    print("list -a")

    os.system('pwd')
    print("result")

def main():
    # seconds = 1000
    # shutdown(seconds)
    ls_dir()

if __name__ == '__main__':
    main()