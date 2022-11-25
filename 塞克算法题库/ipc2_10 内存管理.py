# -*- codeing = utf-8 -*-
# @Time : 2022/7/17 10:34
# @Author : DongYun
# @File : ipc2_10 内存管理.py
# @Software : PyCharm
n,m,q = list(map(int,input().split()))
res = [0]*(n+1)
num = []
y = []
for _ in range(m):
    num.append(list(map(int,input().split()))[1:])
for i in range(q):
    temp = list(map(int,input().split()))
    if temp[0] == 1:
        res[temp[2]:temp[2]+len(num[temp[1]-1])] = num[temp[1]-1]
    if temp[0] == 2:
        y.append(res[temp[1]])
    if temp[0] == 3:
        x = temp[3] if temp[3]<=len(num[temp[1]-1]) else len(num[temp[1]-1])
        for i in range(temp[2],x):
            num[temp[1]-1][i-1] = (num[temp[1]-1][i-1]+1)%256
for i in y:
    print(i)