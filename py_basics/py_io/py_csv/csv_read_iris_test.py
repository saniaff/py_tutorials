#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
author= "huangtw"
ctime = 2017/02/21
"""
import csv
from os.path import dirname
import numpy as np

module_path = dirname(__file__)

with open('./iris.csv') as csv_file:
    data_file = csv.reader(csv_file)
    # 读取表头
    temp = next(data_file)
    n_samples = int(temp[0])
    n_features = int(temp[1])
    target_names = np.array(temp[2:])
    data = np.empty((n_samples, n_features))
    target = np.empty((n_samples,), dtype=np.int)

    # 读取数据
    for i, ir in enumerate(data_file):
        data[i] = np.asarray(ir[:-1], dtype=np.float64)
        target[i] = np.asarray(ir[-1], dtype=np.int)

    print("shape-data", data.shape)
    print("target-data", target.shape)
    print("n_samples", n_samples)