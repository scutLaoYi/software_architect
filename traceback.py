#!/var/bin/python
# -*- coding:cp936 -*-
#Filename : returnStyle.py
import os
import sys
import checkOk
import timeit

solutionCount = [0,]

def search(level, totalLevel, gameMap):
	u"""
	搜索主函数，
	遍历当前层的所有位置，
	找出可能位置并继续下层搜索
	"""
	global solutionCount
	if level == totalLevel:
		for i in range(1, totalLevel + 1):
			gameMap[level] = i
			if checkOk.isOk(gameMap, level, gameMap[level]):
				#print gameMap[1:]
				solutionCount[0] += 1
	else:
		for i in range(1, totalLevel + 1):
			gameMap[level] = i
			if checkOk.isOk(gameMap, level, gameMap[level]):
				search(level + 1, totalLevel, gameMap)


if __name__ == '__main__':
	u"""
	软件架构实验：N皇后问题--回溯法
	time: 2013-10-31 version:0.1b1
	creator: scutLaoYi
	language: Python 2.7
	"""

	totalLevel = int(sys.argv[1])
	totalTimes = int(sys.argv[2])

	assert(totalLevel > 0 and totalLevel < 12)
	assert(totalTimes > 0 and totalTimes < 1000)

	print u"N皇后问题，回溯风格，N =", totalLevel
	time = timeit.timeit(
			"""
	gameMap = range(0, totalLevel+1)
	solutionCount[0] = 0
	search(level = 1, totalLevel = totalLevel, gameMap = gameMap)
			""",
			setup = 'from __main__ import search, totalLevel, solutionCount', 
			number = totalTimes)

	print u'测试次数：', totalTimes
	print u'总用时：', time
	print u'平均用时：',time / totalTimes
	print u"解法总数 =",solutionCount[0]

