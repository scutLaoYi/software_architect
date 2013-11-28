#!/var/bin/python
# -*- coding:cp936 -*-
#Filename : returnStyle.py
import os
import sys
import checkOk

solutionCount = 0

def search(level, totalLevel, gameMap):
	u"""
	������������
	������ǰ�������λ�ã�
	�ҳ�����λ�ò������²�����
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
	����ܹ�ʵ�飺N�ʺ�����--���ݷ�
	time: 2013-10-31 version:0.1b1
	creator: scutLaoYi
	language: Python 2.7
	"""

	totalLevel = 4;
	try:
		totalLevel = int(sys.argv[1])	
		if totalLevel > 10:
			print u"��������ʹ��Ĭ�ϲ���4"
			totalLevel = 4
	except:
		totalLevel = 4
		print u"�����в�������ʹ��Ĭ�ϲ���4"

	print u"N�ʺ����⣬���ݷ��N =", totalLevel
	gameMap = range(0, totalLevel+1)
	search(level = 1, totalLevel = totalLevel, gameMap = gameMap)
	print u"�ⷨ���� =",solutionCount

