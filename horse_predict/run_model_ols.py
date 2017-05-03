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
    pred_y = regr.predict(train_x)
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


import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# Create linear regression object
regr = linear_model.LinearRegression()
# Train the model using the training sets
regr.fit(train_x, train_y)
# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % np.mean((regr.predict(test_x) - test_y) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(test_x, test_y))


## step 3: testi


# method2
model_evalute(train_x, train_y)
model_evalute(test_x, test_y)

# ss = sum((pred_y-train_y)**2)/total

# from sklearn.metrics import accuracy_score
# pred_y2 = array(pred_y2)
# acc2 = accuracy_score(train_y,pred_y2)
# print "acc2", acc2

# accuracy = regr.predict(train_x, train_y)
# print 'The classify accuracy(close test) is: %.3f%%' % (accuracy * 100)
# accuracy = regr.predict(test_x, test_y)
# print 'The classify accuracy(open test) is: %.3f%%' % (accuracy * 100)
# # Plot outputs
# plt.scatter(test_x, test_y,  color='black')
# plt.plot(test_x, regr.predict(test_x), color='blue',
#          linewidth=3)
#
# plt.xticks(())
# plt.yticks(())
#
# plt.show()