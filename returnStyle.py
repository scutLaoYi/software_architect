#!/var/bin/python
# -*- coding:cp936 -*-
#Filename : returnStyle.py
import os
import sys

global solutionCount

def checkOK(level, gameMap):
	u"""检测当前状态是否与已有的皇后冲突
		冲突存在则返回False,
		否则返回True
		"""
	nowPos = gameMap[level]
	for i in range(1, level):
		levelPos = gameMap[level - i]
		if levelPos == nowPos or \
					 levelPos == nowPos - i or \
					 levelPos == nowPos + i:
			return False
	return True

def search(level, totalLevel, gameMap):
	u"""
	搜索主函数，
	遍历当前层的所有位置，
	找出可能位置并继续下层搜索
	"""
	if level == totalLevel:
		for i in range(1, totalLevel + 1):
			gameMap[level] = i
#			print "Testing...", i
			if checkOK(level, gameMap):
				print "found!", gameMap[1:]
#				solutionCount += 1
	else:
		for i in range(1, totalLevel + 1):
			gameMap[level] = i
			if checkOK(level, gameMap):
#				print "Searching at level %d position: %d" % (level, i)
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

	print u"程序运行中..."
	print u"检测%d皇后问题的解法..." % totalLevel
	gameMap = range(0, totalLevel+1)
	search(level = 1, totalLevel = totalLevel, gameMap = gameMap)
#	print u"解法总数：%d" % solutionCount

