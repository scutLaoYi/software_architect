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
	#��������һ��Ŀ��н�
	for nowSolution in nowList[nowLevel-1]:
		#�������ڿ��н��µ�ǰ�������λ��
		for i in range(1, totalLevel + 1):
			#���ҵ��µĿ��н⣬���¼����ǰ��Ŀ��н⼯��
			if checkOk.isOk(nowSolution, nowLevel, i):
				tmpList = nowSolution[:]
				tmpList.append(i)
				solutionInThisLevel.append(tmpList)
	#����ǰ��Ŀ��н��¼���ܽ⼯��
	nowList.append(solutionInThisLevel)
	return nowList

def search(totalLevel):
	u"""
	��������
	����ʺ��N�����ز��ҵĽ��
	"""
	possibleList = []

#	��ʼ�����ܵ�ֵ������ܵ�
	for i in range(1, totalLevel + 1):
		possibleList.append([0, i])
	nowList = [0, possibleList]

#	ͨ�������ˣ���ȡ���յĽ⼯����
	for i in range(2, totalLevel+1):
		nowList = queenPipe(nowList, totalLevel, i)

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

	print u"N�ʺ����⣬�ܵ����N =", totalLevel
	totalAmout = [0,];
	time = timeit.timeit('totalAmout[0] = search(totalLevel)', setup="from __main__ import totalAmout, search, totalLevel", number = totalTimes)
	print u'���Դ�����', totalTimes
	print u'����ʱ��', time
	print u'ƽ����ʱ��',time / totalTimes
	print u"�ⷨ���� =", totalAmout[0]
