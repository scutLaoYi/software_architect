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
	������������
	������ǰ�������λ�ã�
	�ҳ�����λ�ò������²�����
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
	����ܹ�ʵ�飺N�ʺ�����--���ݷ�
	time: 2013-10-31 version:0.1b1
	creator: scutLaoYi
	language: Python 2.7
	"""

	totalLevel = int(sys.argv[1])
	totalTimes = int(sys.argv[2])

	assert(totalLevel > 0 and totalLevel < 12)
	assert(totalTimes > 0 and totalTimes < 1000)

	print u"N�ʺ����⣬���ݷ��N =", totalLevel
	time = timeit.timeit(
			"""
	gameMap = range(0, totalLevel+1)
	solutionCount[0] = 0
	search(level = 1, totalLevel = totalLevel, gameMap = gameMap)
			""",
			setup = 'from __main__ import search, totalLevel, solutionCount', 
			number = totalTimes)

	print u'���Դ�����', totalTimes
	print u'����ʱ��', time
	print u'ƽ����ʱ��',time / totalTimes
	print u"�ⷨ���� =",solutionCount[0]

