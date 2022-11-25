# -*- codeing = utf-8 -*-
# @Time : 2022/7/17 15:37
# @Author : DongYun
# @File : 1.6.4 棋盘问题2.py
# @Software : PyCharm
m,n = list(map(int,input().split()))
grid = [[-1]*m for i in range(m)]
for _ in range(n):
    temp = list(map(int, input().split()))
    grid[temp[0]-1][temp[1]-1] = temp[2]
print(grid)
def dfs():
