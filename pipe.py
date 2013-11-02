#!/var/bin/python
# -*- coding:cp936 -*-
#filename:pipe.py

import os
import sys

def isOk(nowMap, nowLevel, nowPos):
	u"""
	��⵱ǰ״̬�Ƿ������еĻʺ��ͻ
		��ͻ�����򷵻�False,
		���򷵻�True
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
	������
	���뵱ǰ�Ŀ��ܽ⼯������ɸѡ����ȡ��һ������п��ܽ⼯������
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
	print u"�⼯ in this level:", solutionInThisLevel
	return nowList

def search(totalLevel):
	u"""
	��������
	����ʺ��N�����ز��ҵĽ��
	"""
	possibleList = []
	for i in range(1, totalLevel + 1):
		possibleList.append([0, i])
	nowList = [0, possibleList]
#	��ʼ�����ܵ�ֵ������ܵ�

	for i in range(2, totalLevel+1):
		nowList = queenPipe(nowList, totalLevel, i)
#	ͨ�������ˣ���ȡ���յĽ⼯����

	return len(nowList[totalLevel])

if __name__ == "__main__":
	u"""
	����ܹ�ʵ�飺N�ʺ�����--�ܵ����
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

