#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
mtime= "16-5-19"
"""
from collections import defaultdict
from numpy import array,random

def read_vec_bin(file,reg):
    '''
    词向量的映射文件读取
    :param file: 二进制文件
    :param reg: 向量分隔符号
    :return: 词向量的map,词向量的条数
    '''
    w2v_map = defaultdict(float)
    # datas = zeros((ret_arr.shape[0], ret_arr.shape[1], vocab_size))
    fr = open(file, 'r')
    i = 0
    for line in fr.readlines():
        i +=1
        if i==1:#去除第一行
            dim = line.split(',')[1].strip()
            continue
        # print("no",i,"line",line)
        aa = line.split()
        # print("word",aa[0])
        # print aa[1]
        vecs = aa[1].split(reg)
        w2v_map[aa[0]]=vecs #看需不需要转化为numpy类型
        # print("vecs",vecs)
    fr.close()
    return dim,i-1,w2v_map



def padding_sequences(lines, max_len, value, regStr):
    '''
    给指定的句子进行长度补齐操作
    :param lines:
    :param max_len:
    :param value:
    :param regStr: 补齐的拼接字符串
    :return:
    '''
    ret = []
    record_nums = 0
    for line in lines:
        list = line.split()
        # print("line",line,"list",list,"size",len(list))
        row_len = len(list)
        if row_len>=max_len:##进行截取操作
            list = list[:max_len]
        else:##进行补齐操作
            for i in range(max_len-row_len):
                list.append(value)
        # line = regStr.join(list[:max_len])
        # line = line[len(regStr):]
        # # print("newLine",line)
        # ret.append(line)

        ret.append(list[:max_len])
        record_nums = record_nums + 1
    return record_nums, ret


def read_corpus(corpus_name, wordvec_name, vec_reg, max_len, is_positive=True):
    '''
    读取原始语料
    :param corpus_name:语料名称
    :param wordvec_name: 词向量文件
    :param vec_reg: 词向量分割文件
    :param max_len: 输入的最大长度
    :param is_positive: 是否是正例文件
    :return: 语料行数*最大长度*词向量的维度 --训练数据
    '''
    print('padding row.....')
    fr = open(corpus_name,'r')
    lines = fr.readlines()
    rows,lines = padding_sequences(lines, max_len=max_len, value='UNK',regStr = ' ')

    print('reading wordvec....')
        ##期望值
    data_y = [1 if is_positive else 0 for i in range(rows)]
    print("y",data_y)
    ##加载词向量文件
    dim, _,w2v_map = read_vec_bin(wordvec_name,vec_reg)
    ##实际的训练数据
    # data_x = array((rows, max_len, dim),dtype='float64')
    print("rows",rows,"max_len",max_len,"dim",dim)
    data_x = []
    for row_num in range(rows):
        for word_num in range(max_len):
            # print("row_num",row_num,"word_num",word_num)
            word = lines[row_num][word_num]
            vec = None
            if vec==None:
                vec = random.uniform(-0.025,0.025,300)
                # print("word",word,"vec",vec)
            else:
                pass
                # print("word",word,"vec",vec)
            ###如何将数据装进入
            # data_x[row_num][word_num] = array(vec)
            data_x.extend(vec)
    xx = array(data_x,dtype='float64')
    # print("xx",xx)
    print("xx-len",len(xx))
    yy = xx.reshape((int(rows),int(max_len),int(dim)))
    return yy,data_y


####验证读取词向量
# file = 'vectors_mini.bin'
# reg = ','
# dim,i,w2v_map = read_vec_bin(file,reg)
# print("vocab",i,"dim",dim)
# word = 'spiders'
# print("word",word,"vec",w2v_map.get(word))

# ##验证padding
# lines = open('line.txt').readlines()
# max_len = 10
# value = 'UNK'
# regStr = ' '
# num_records,new_lines = padding_sequences(lines, max_len, value, regStr)
# print("num_records",num_records)
# for line in new_lines:
#     print line

##验证向量的读取
# corpus_name = 'line.txt'
# wordvec_name = 'vectors.bin'
# vec_reg = ','
# max_len = 10
#
# data_x,data_y = read_corpus(corpus_name, wordvec_name, vec_reg, max_len, is_positive=True)
# print data_y
# print data_x.shape