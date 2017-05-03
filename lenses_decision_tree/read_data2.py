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
    for i in range(size):
        s = currLine[i]

        # 针对第一个元素特殊处理
        if i == 0:
            if len(s) > 1:
                s = s.split(' ')[1]
            else:
                continue

        lineArr.append(s)

    trainingSet.append(lineArr)
    trainingLabels.append(currLine[size])

print '-'*100
for s in trainingSet:
    print s
# import pprint
# print "train-data", pprint.pprint(trainingSet)
print "label", trainingLabels
