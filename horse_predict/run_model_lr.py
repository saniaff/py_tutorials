# -*- coding: utf-8 -*-
"""
author = 'sania'
ctime = 2017/05/01
"""

from numpy import *

def load_horse_colic(filename):
    """
    数据载入
    :param filename:
    :return:
    """
    frTrain = open(filename)
    trainingSet = []
    trainingLabels = []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        lineArr.append(1.0)  # 开始加一个1,用于学习偏置bias
        for i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[21]))
    return array(trainingSet), array(trainingLabels)
    # return mat(trainingSet), mat(trainingLabels).transpose()

def model_evalute(train_x, train_y):
    pred_y = model.predict(train_x)
    # print "pred_y", pred_y
    total = len(train_y)
    right = 0
    # pred_y2 = []
    for i in range(total):
        cur_y = pred_y[i]
        if cur_y > 0.5:
            cur_y = 1
        else:
            cur_y = 0
        # pred_y2.append(cur_y)
        if cur_y == train_y[i]:
            right += 1
    print "right", right, "total", total
    # print "acc", right/total
    print "acc", float(float(right) / total)

# step 1: load data
print "step 1: load data..."
train_x, train_y = load_horse_colic('data/horseColicTraining.txt')
test_x, test_y = load_horse_colic('data/horseColicTest.txt')
print("train_x-shape", train_x.shape, "train_y-shape", train_y.shape)
print("test_x-shape", test_x.shape, "test_y-shape", test_y.shape)


import numpy as np

from sklearn.linear_model import LogisticRegression

# Create linear regression object
model = LogisticRegression(max_iter=3000000, C=0.001, penalty='l2')
# Train the model using the training sets
model.fit(train_x, train_y)

## step 3: testi

# method1
model_evalute(train_x, train_y)
print "**"*100
model_evalute(test_x, test_y)

print "--"*100

score = model.score(train_x, train_y)
print "train-score", score

print "."*100
score_t = model.score(test_x,test_y)
print "test-score",score_t