#!/var/bin/python
# -*- coding:cp936 -*-
#filename:pipe.py

import os
import sys
import checkOk 
import timeit

def queenPipe(nowList, totalLevel, nowLevel):
	u"""
	过滤器
	传入当前的可能解集，进行筛选，获取新一层的所有可能解集并返回
	"""
	solutionInThisLevel = []
	for nowSolution in nowList[nowLevel-1]:
		for i in range(1, totalLevel + 1):
			if checkOk.isOk(nowSolution, nowLevel, i):
				tmpList = nowSolution[:]
				tmpList.append(i)
				solutionInThisLevel.append(tmpList)
	nowList.append(solutionInThisLevel)
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
	#for solu in nowList[totalLevel]:
		#print solu[1:]

	return len(nowList[totalLevel])

if __name__ == "__main__":
	u"""
	软件架构实验：N皇后问题--管道风格
	time: 2013-11-01 version:0.1b1
	creator: scutLaoYi
	language: Python 2.7
	"""
	totalLevel = int(sys.argv[1])
	totalTimes = int(sys.argv[2])

	assert(totalLevel > 0 and totalLevel < 12)
	assert(totalTimes > 0 and totalTimes < 1000)
	
	print u"N皇后问题，管道风格，N =", totalLevel
	totalAmout = [0,];
	time = timeit.timeit('totalAmout[0] = search(totalLevel)', setup="from __main__ import totalAmout, search, totalLevel", number = totalTimes)
	print u'测试次数：', totalTimes
	print u'总用时：', time
	print u'平均用时：',time / totalTimes
	print u"解法总数 =", totalAmout[0]
