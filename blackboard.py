#!/var/bin/python
# -*- coding:utf-8 -*-
#filename: board.py

import os
import sys
import checkOk
import timeit

counter = 0

def createPlayer(level, totalLevel):
	u"""
	黑板玩家创建函数
	创建并返回闭包
	每个闭包为单独一层黑板的绘制者
	检测当前状态是否正确，返回结果
	"""
	def playerFunction(gameBoard):
		while gameBoard[level] < totalLevel:
			gameBoard[level] += 1
			if checkOk.isOk(gameBoard, level, gameBoard[level]):
				return True
		gameBoard[level] = 0
		return False
	return playerFunction

def searchRun(totalLevel):
	global counter;
	gameBoard = [0]
	playerList = [0,]
	for i in range(1, totalLevel + 1):
		playerList.append(createPlayer(i, totalLevel))
		gameBoard.append(0)
	
	nowLevel = 1
	counter = 0
	while nowLevel > 0:
		if playerList[nowLevel](gameBoard): 
			if nowLevel < totalLevel:
				nowLevel += 1
			else:
				#print gameBoard[1:]
				counter += 1
		else:
			nowLevel -= 1

if __name__ == '__main__':
	u"""
	软件架构实验：N皇后问题--黑板风格
	time: 2013-11-03 version:0.1b1
	creator: scutLaoYi
	language: Python 2.7
	"""

	totalLevel = int(sys.argv[1])
	totalTimes = int(sys.argv[2])

	assert(totalLevel > 0 and totalLevel < 12)
	assert(totalTimes > 0 and totalTimes < 1000)

	print "N皇后问题，黑板风格，N =", totalLevel
	
	time = timeit.timeit("""
		counter = 0
		searchRun(totalLevel)
			""", 
			setup="from __main__ import totalLevel, counter, searchRun", 
			number = totalTimes)

	print u'测试次数：', totalTimes
	print u'总用时：', time
	print u'平均用时：',time / totalTimes
	print u"解法总数 =", counter


