# -*- coding: utf-8 -*-
"""
author = 'sania'
ctime = 2017/05/02
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

from sklearn.tree import DecisionTreeClassifier
# Create linear regression object
model = DecisionTreeClassifier()
# Train the model using the training sets
model.fit(train_x, train_y)

score = model.score(train_x, train_y)
print "train-score", score
score_t = model.score(test_x, test_y)
print "test-score", score_t