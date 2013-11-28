#!/usr/bin/python
# -*- encoding=utf-8 -*-

def isOk(nowMap, nowLevel, nowPos):
	u"""
	检测当前状态是否与已有的皇后冲突
		冲突存在则返回False,
		否则返回True
		"""
	for i in range(1, nowLevel):
		levelPos = nowMap[nowLevel - i]
		if levelPos == nowPos or \
					 levelPos == nowPos - i or \
					 levelPos == nowPos + i:
			return False
	return True
