#!/usr/bin/python3

import numpy as np
import operator
import sys
import os
import math

def createDataSet(fileN):
	path = "./" + fileN

	#groupArray = np.array([])
	groupArray = np.empty((0,1024),int)
	labelList = []
	#buff = np.array([])
	for filename in os.listdir(path):
		fName = path + filename

		l = filename.split('_')
		labelList.append(l[0])

		data = ""
		with open( os.path.join(path,filename) , "rt") as f:
			data = f.read().replace("\n","")
			# int로 데이터 넣기	
			dList = np.array([])
			for d in list(data):
				num = int(d)
				dList = np.append(dList, num)		

			fData = np.array([dList])
			groupArray = np.append(groupArray, fData, axis=0 )

	return groupArray, labelList




def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = np.zeros(np.shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - np.tile(minVals, (m, 1))
	normDataSet = normDataSet / np.tile(ranges, (m, 1))
	return normDataSet, ranges, minVals



def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX,(dataSetSize,1))-dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances ** 0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.items(),
		key = operator.itemgetter(1), reverse = True)
	return sortedClassCount[0][0]




training = str(sys.argv[1])
test = str(sys.argv[2])


tGroup, tLabels = createDataSet(training)
group,labels = createDataSet(test)

for i in range(1,21):
	wrong = 0
	all = 0
	k = 0
	for j in group:
		all = all + 1
		result =  classify0(j, tGroup, tLabels, i)
		if labels[k] != result:
			wrong = wrong + 1
		k = k + 1
		
	print( math.trunc((wrong/all) * 100))
