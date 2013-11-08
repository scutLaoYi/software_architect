#!/var/bin/python
# -*- coding:utf-8 -*-
#filename: board.py

import os
import sys

def isOk(gameMap, level, nowPos):
	u"""检测当前状态是否与已有的皇后冲突
		冲突存在则返回False,
		否则返回True
		"""
	for i in range(1, level):
		levelPos = gameMap[level - i]
		if levelPos == nowPos or \
					 levelPos == nowPos - i or \
					 levelPos == nowPos + i:
			return False
	return True


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
			if isOk(gameBoard, level, gameBoard[level]):
				return True
		gameBoard[level] = 0
		return False
	return playerFunction

if __name__ == '__main__':
	u"""
	软件架构实验：N皇后问题--黑板风格
	time: 2013-11-03 version:0.1b1
	creator: scutLaoYi
	language: Python 2.7
	"""
	playerList = [0]
	totalLevel = 4
	gameBoard = [0]
	for i in range(1, totalLevel + 1):
		playerList.append(createPlayer(i, totalLevel))
		gameBoard.append(0)
	
	nowLevel = 1
	while nowLevel > 0:
		if playerList[nowLevel](gameBoard): 
			if nowLevel < totalLevel:
				nowLevel += 1
			else:
				print "found! ", gameBoard
		else:
			nowLevel -= 1

	

