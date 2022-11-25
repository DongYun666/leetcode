# -*- codeing = utf-8 -*-
# @Time : 2022/7/13 15:48
# @Author : DongYun
# @File : 1.3.1全排列问题.py
# @Software : PyCharm

def han(n,A,B,C):
	if n == 1:
		print("Move disk "+str(n)+" from "+A+" to "+C)
	else:
		han(n-1,A,C,B)
		print("Move disk "+str(n)+" from "+A+" to "+C)
		han(n-1,B,A,C)

n = int(input())
han(n,'A','B','C')
