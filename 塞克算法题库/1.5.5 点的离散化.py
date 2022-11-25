# -*- codeing = utf-8 -*-
# @Time : 2022/7/15 16:27
# @Author : DongYun
# @File : 1.5.5 点的离散化.py
# @Software : PyCharm
# n = int(input())
# num = []
# for i in range(n):
#     temp = list(map(int, input().split()))
#     num.append((temp[0],temp[1]))
# tempNum = list(range(1,len(num)+1))
# dct = dict(zip(num,tempNum))
# num.sort(key=lambda x:(x[0],x[1]))
# res = []
# for i in range(n):
#     print(num[i][0],end=" ")
#     print(num[i][1])
#     res.append(dct[num[i]])
# for i in range(len(res)):
#     print(res[i],end=" ")
import functools


class Node(object):
    def __init__(self,x,y,pos):
        self.x = x
        self.y = y
        self.pos = pos
def cmp(a,b):
    if a.x!=b.x:
        return a.x - b.x
    if a.y!=b.y:
        return a.y - b.y
    return a.pos - b.pos
n = int(input())
num = []
for i in range(n):
    temp = list(map(int, input().split()))
    num.append(Node(temp[0],temp[1],i))
num = sorted(num,key = functools.cmp_to_key(cmp))
res = [0]*len(num)
for i in range(0,n):
    print(num[i].x,end=" ")
    print(num[i].y)
    res[num[i].pos] = i + 1
for i in range(len(res)):
    print(res[i],end=" ")

