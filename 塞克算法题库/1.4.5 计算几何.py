# -*- codeing = utf-8 -*-
# @Time : 2022/7/14 11:51
# @Author : DongYun
# @File : 1.4.5 计算几何.py
# @Software : PyCharm
from 美团笔试4 import mid

n = int(input())
uncle_x = list(map(int,input().split()))
uncle_y = list(map(int,input().split()))
uncle_x.sort()
uncle_y.sort()
m = int(input())
for i in range(m):
    temp = list(map(int, input().split()))
    l,r = 1,n
    while l<r:
        mid = (l+r)//2
        if
