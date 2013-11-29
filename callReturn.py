#!/usr/bin/python
# -*- encoding=utf-8 -*-

import os
import sys
import timeit

#记录总数
totalAmout = 0
#记录满状态的棋盘
complete = 1

def search(curPos, leftConf, rightConf):
	u"""
	用于搜索的函数
	使用算法：二进制法
	curPos记录当前已被放置皇后的位置（对应位为1）
	leftConf记录当前层左上方冲突的位置
	rightConf记录当前层右上方冲突的位置
	"""
	global totalAmout
	global complete

	#若所有位置都放置了皇后，说明找到了一个可行的解
	if curPos == complete:
		totalAmout += 1
	else:
		#找出当前层的所有可能放置皇后的位置
		#三个数值做或运算找出所有冲突的位置（对应位为1），取反得到所有可能放置位置（1）
		#与满棋盘状态进行与运算，排除超出N的部分（满棋盘状态最右N个位置为1）
		#得到所有可能的放置位置
		pos = complete & ~(curPos | leftConf | rightConf)
		#逐个搜索可能位置
		while pos != 0:
			#找出最右的第一个位置
			rightMost = pos & -pos
			#在可能解中去除当前位置
			pos -= rightMost
			#递归搜索当前位置的下一层可能解
			#在已放置皇后的位置加入当前位置
			#该位置与左上方及右上方位置冲突
			#左右移位将历史记录中的冲突位置更新
			search(curPos + rightMost, 
					(leftConf + rightMost) << 1, 
					(rightConf + rightMost) >> 1)

if __name__ == '__main__':
	totalLevel = int(sys.argv[1])			
	totalTimes = int(sys.argv[2])

	print u"N皇后问题， 调用返回风格， N =", totalLevel

	#获取当前N的满棋盘状态（最右N位均为1，其他位置为0）
	complete = (complete << totalLevel) - 1
	time = timeit.timeit(
			'search(0, 0, 0)', 
			setup="from __main__ import search, totalLevel", 
			number = totalTimes)
	print u'测试次数：', totalTimes
	print u'总用时：', time
	print u'平均用时：',time / totalTimes
	print u"解法总数 =", totalAmout
	
