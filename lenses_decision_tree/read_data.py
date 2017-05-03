# -*- coding: utf-8 -*-
"""
author = 'sania'
ctime = 2017/05/03
"""
# from sklearn.trees import

fr = open('a')
trainingSet = []
trainingLabels = []
for line in fr.readlines():
    currLine = line.strip().split('  ')
    print currLine
    lineArr = []

    size = len(currLine)-1
    for i in range(3):
        lineArr.append(currLine[size-i-1])

    s = currLine[size-4]
    if len(s)==1:
        s = s
    else:
        s = s.split(' ')[1]

    lineArr.append(s)
    lineArr = lineArr[::-1]
    trainingSet.append(lineArr)
    trainingLabels.append(currLine[size])

# print '-'*100
# for s in trainingSet:
#     print s
# # import pprint
# # print "train-data", pprint.pprint(trainingSet)
# print "label", trainingLabels
import numpy as np
trainingSet = np.array(trainingSet)
trainingLabels = np.array(trainingLabels)

from sklearn.tree import DecisionTreeClassifier
# Create linear regression object
model = DecisionTreeClassifier()
# Train the model using the training sets
model.fit(trainingSet, trainingLabels)

score = model.score(trainingSet, trainingLabels)
print "train-score", score