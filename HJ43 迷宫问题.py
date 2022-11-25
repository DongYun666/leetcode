# -*- codeing = utf-8 -*-
# @Time : 2022/4/16 20:46
# @Author : DongYun
# @File : HJ43 迷宫问题.py
# @Software : PyCharm
from typing import List



migong = []

def work(i, j,res = [(0,0)]):
    if i + 1 < M and migong[i+1][j] == 0 and (i+1,j) not in res:  # 右
        work(i+1, j, res+[(i+1,j)])
    if i-1 >=0 and migong[i-1][j] == 0 and (i-1,j) not in res:  # 左
        work(i-1, j, res+[(i-1,j)])
    if j + 1 < N and migong[i][j+1] == 0 and (i,j+1) not in res:  # 上
        work(i, j + 1, res+[(i,j+1)])
    if j - 1 >= 0 and migong[i][j-1] == 0 and (i,j-1) not in res:  # 下
        work(i, j + 1, res+[(i,j-1)])
    if (i,j) == (N-1,M-1):
        for s in res:
            print("("+str(s[0])+","+str(s[1])+")")
while True:
    try:
        N, M = list(map(eval, input().split()))
        for _ in range(N):
            temp = list(map(int, input().split()))
            migong.append(temp)
        print(migong)
        work(0,0)
    except:
        break
