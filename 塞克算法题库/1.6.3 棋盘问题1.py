# -*- codeing = utf-8 -*-
# @Time : 2022/7/17 15:10
# @Author : DongYun
# @File : 1.6.3 棋盘问题1.py
# @Software : PyCharm
from Tools.scripts.findlinksto import visit

n,k = 0,0
res = []
while n!=-1 and k!=-1:
    n, k = list(map(int, input().split()))
    grid = []
    for _ in range(n):
        string = input()
        temp = []
        for s in string:
            temp.append(s)
        grid.append(temp)
    visited = [0]*n
    count = 0
    def dfs(cur):
        global k
        if k == 0:
            global count
            count+=1
            return
        if cur >= n:return
        for i in range(n):
            if visited[i] == 0 and grid[cur][i] == "#":
                visited[i] = 1
                k-=1
                dfs(cur+1)
                k+=1
                visited[i] = 0
        dfs(cur+1)
    dfs(0)
    res.append(count)
for i in res[:-1]:
    print(i)