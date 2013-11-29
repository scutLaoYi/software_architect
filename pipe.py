#!/var/bin/python
# -*- coding:cp936 -*-
#filename:pipe.py

import os
import sys
import checkOk 
import timeit

def queenPipe(nowList, totalLevel, nowLevel):
	u"""
	������
	���뵱ǰ�Ŀ��ܽ⼯������ɸѡ����ȡ��һ������п��ܽ⼯������
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
	#for solu in nowList[totalLevel]:
		#print solu[1:]

	return len(nowList[totalLevel])

if __name__ == "__main__":
	u"""
	����ܹ�ʵ�飺N�ʺ�����--�ܵ����
	time: 2013-11-01 version:0.1b1
	creator: scutLaoYi
	language: Python 2.7
	"""
	totalLevel = int(sys.argv[1])
	totalTimes = int(sys.argv[2])

	assert(totalLevel > 0 and totalLevel < 12)
	assert(totalTimes > 0 and totalTimes < 1000)
	
	print u"N�ʺ����⣬�ܵ����N =", totalLevel
	totalAmout = [0,];
	time = timeit.timeit('totalAmout[0] = search(totalLevel)', setup="from __main__ import totalAmout, search, totalLevel", number = totalTimes)
	print u'���Դ�����', totalTimes
	print u'����ʱ��', time
	print u'ƽ����ʱ��',time / totalTimes
	print u"�ⷨ���� =", totalAmout[0]
