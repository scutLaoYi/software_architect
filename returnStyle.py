#!/var/bin/python
# -*- coding:cp936 -*-
#Filename : returnStyle.py
import os
import sys

global solutionCount

def checkOK(level, gameMap):
	u"""��⵱ǰ״̬�Ƿ������еĻʺ��ͻ
		��ͻ�����򷵻�False,
		���򷵻�True
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
	������������
	������ǰ�������λ�ã�
	�ҳ�����λ�ò������²�����
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

	print u"����������..."
	print u"���%d�ʺ�����Ľⷨ..." % totalLevel
	gameMap = range(0, totalLevel+1)
	search(level = 1, totalLevel = totalLevel, gameMap = gameMap)
#	print u"�ⷨ������%d" % solutionCount

