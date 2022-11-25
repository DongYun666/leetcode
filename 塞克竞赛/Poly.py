# -*- codeing = utf-8 -*-
# @Time : 2022/7/24 14:00
# @Author : DongYun
# @File : Poly.py
# @Software : PyCharm
from math import sqrt

C = int(input())
temp = []
for i in range(1,C):
    for j in range(1,C):
        x = sqrt(i**2+j**2)
        if x % 1 == 0 and x not in temp and x<C:
            print(i, j)
            temp.append(int(x))

print(temp)