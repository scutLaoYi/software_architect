#!/usr/bin/python
# -*- encoding=utf-8 -*-

import os
import sys

if __name__ == '__main__':
	u"""
	软件架构实验：N皇后问题 主程序
	time:2013-11-29 version:0.1a1
	creator: scutLaoYi
	language: Python 2.7
	"""
	funcDict = {
			0:'callReturn',
			1:'pipe',
			2:'traceback',
			3:'blackboard'
			}

	totalLevel = input('N = ')
	totalTimes = input('Testing times = ')
	print """
	Choose a style:
	0:call and return
	1:pipe
	2:traceback
	3:blackboard
	others:exit
	"""
	style = input('Choose one:')

	styleName = funcDict.get(style, 'null')
	if styleName == 'null':
		sys.exit(0)

	cmd = 'python '+ styleName + '.py' + ' %d %d' % (totalLevel, totalTimes)
	os.system(cmd) 
