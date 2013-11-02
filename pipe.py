#!/var/bin/python
# -*- coding:cp936 -*-
#filename:pipe.py

import os
import sys

def isOk(nowMap, nowLevel, nowPos):
	u"""
	检测当前状态是否与已有的皇后冲突
		冲突存在则返回False,
		否则返回True
		"""
	for i in range(1, nowLevel):
		levelPos = nowMap[nowLevel - i]
		if levelPos == nowPos or \
					 levelPos == nowPos - i or \
					 levelPos == nowPos + i:
			return False
	return True


def queenPipe(nowList, totalLevel, nowLevel):
	u"""
	过滤器
	传入当前的可能解集，进行筛选，获取新一层的所有可能解集并返回
	"""
	solutionInThisLevel = []
	print "level:%d" % nowLevel
	for nowSolution in nowList[nowLevel-1]:
		for i in range(1, totalLevel + 1):
			if isOk(nowSolution, nowLevel, i):
				tmpList = nowSolution[:]
				tmpList.append(i)
				solutionInThisLevel.append(tmpList)
	nowList.append(solutionInThisLevel)
	print u"解集 in this level:", solutionInThisLevel
	return nowList

def search(totalLevel):
	u"""
	搜索函数
	传入皇后的N，返回查找的结果
	"""
	possibleList = []
	for i in range(1, totalLevel + 1):
		possibleList.append([0, i])
	nowList = [0, possibleList]
#	初始化可能的值，传入管道

	for i in range(2, totalLevel+1):
		nowList = queenPipe(nowList, totalLevel, i)
#	通过逐层过滤，获取最终的解集数量

	return len(nowList[totalLevel])

if __name__ == "__main__":
	u"""
	软件架构实验：N皇后问题--管道风格
	time: 2013-11-01 version:0.1b1
	creator: scutLaoYi
	language: Python 2.7
	"""
	totalLevel = 4
	try:
		totalLevel = int(sys.argv[1])
		if totalLevel > 10:
			print "illegal argument!"
			totalLevel = 4
	except :
		totalLevel = 4
		print "illegal argument!"
	
	print "total amount:", search(totalLevel)
	print "N=%d" % totalLevel

