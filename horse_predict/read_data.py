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


## step 3: testing
def sigmoid(inX):
    return 1.0 / (1 + exp(-inX))
def evaluate(weights, test_x, test_y):
    '''
    模型评估
    :param weights:
    :param test_x:
    :param test_y:
    :return:
    '''
    numSamples, numFeatures = shape(test_x)
    matchCount = 0
    for i in xrange(numSamples):
        predict = sigmoid(test_x[i, :] * weights)[0, 0] > 0.5
        if predict == bool(test_y[i, 0]):
            matchCount += 1
    accuracy = float(matchCount) / numSamples
    return accuracy

accuracy = evaluate(regr, train_x, train_y)
print 'The classify accuracy(close test) is: %.3f%%' % (accuracy * 100)
# # Plot outputs
# plt.scatter(test_x, test_y,  color='black')
# plt.plot(test_x, regr.predict(test_x), color='blue',
#          linewidth=3)
#
# plt.xticks(())
# plt.yticks(())
#
# plt.show()