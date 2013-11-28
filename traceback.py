#!/var/bin/python
# -*- coding:cp936 -*-
#Filename : returnStyle.py
import os
import sys
import checkOk

solutionCount = 0

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
				print gameMap[1:]
				solutionCount += 1
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

	totalLevel = 4;
	try:
		totalLevel = int(sys.argv[1])	
		if totalLevel > 10:
			print u"参数过大，使用默认参数4"
			totalLevel = 4
	except:
		totalLevel = 4
		print u"命令行参数错误，使用默认参数4"

	print u"N皇后问题，回溯风格，N =", totalLevel
	gameMap = range(0, totalLevel+1)
	search(level = 1, totalLevel = totalLevel, gameMap = gameMap)
	print u"解法总数 =",solutionCount

