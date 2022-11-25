# -*- codeing = utf-8 -*-
# @Time : 2021/11/25 19:21
# @Author : DongYun
# @File : 鱿鱼游戏1.py
# @Software : PyCharm
import random

dp = [[0 for i in range(7+1)] for j in range(8+1)]
def func(i,j,k,n):
    chose = random.randint(0,1)
    if chose == 1:
        if i == k:
            return 0
        if j == n:
            return k -i+1
        return func(i+1,j+1,k,n)
    else:
        if i == k:
            return 0
        if j == n:
            return k -i
        return func(i,j+1,k,n)

print(func(1,4,7,8))
# print(dp)