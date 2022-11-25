# -*- codeing = utf-8 -*-
# @Time : 2022/7/18 11:31
# @Author : DongYun
# @File : 1.6.6奶酪.py
# @Software : PyCharm
import math

class node:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
res = []
visited = []
num = []
def sqrt(x1,y1,z1,x2,y2,z2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
def dfs(x,y,z,k,n,r,h):
    if z+r>=h:
        global flag
        flag = True
        return
    visited[k] = True
    for i in range(n):
        if sqrt(x,y,z,num[i].x,num[i].y,num[i].z) <=2*r and not visited[i]:
            dfs(num[i].x,num[i].y,num[i].z,i,n,r,h)

T = int(input())
for _ in range(T):
    n,h,r = list(map(int,input().split()))
    num.clear()
    for i in range(n):
        temp = list(map(int, input().split()))
        num.append(node(temp[0],temp[1],temp[2]))
    visited.clear()
    visited = [False] * (n+1)
    for i in range(n):
        flag = False
        if num[i].z-r<=0:
            dfs(num[i].x,num[i].y,num[i].z,i,n,r,h)
            if flag:
                print("Yes")
                break
    if not flag:
        print("No")