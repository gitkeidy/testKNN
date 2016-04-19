
from numpy import *
import operator
from os import listdir

def kClassify(inX,dataMat,label,k):
	dataSize = dataMat.shape[0]	#get matrix's size
	square = (tile(inX,(dataSize,1)) - dataMat)**2
	sumOfSquare = square.sum(axis=1) 
	dist = sumOfSquare**(0.5) #can't use 1/2,why?
	
	distArg = dist.argsort()
	classDict = {}

	for x in range(k):
		classDict[label[distArg[x]]] = classDict.get(label[distArg[x]],0) + 1;
	#return classDict
	selectLabel = sorted(classDict.items(),key=itemgetter(1),reverse=1)
	return selectLabel[0][0]

def img2Vector(fileName):
	imgVect = zeros((1,1024))
	fr = open(fileName)
	for x in range(32):
		lr = fr.readline()
		for y in range(32):
			imgVect[0,x*32+y] = lr[y]
	return imgVect

def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')          
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]     
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2Vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')        
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]     
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2Vector('testDigits/%s' % fileNameStr)
        classifierResult = kClassify(vectorUnderTest, trainingMat, hwLabels, 3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)
        if (classifierResult != classNumStr): errorCount += 1.0
    print "\nthe total number of errors is: %d" % errorCount
    print "\nthe total error rate is: %f" % (errorCount/float(mTest))

	