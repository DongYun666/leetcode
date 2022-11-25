# -*- codeing = utf-8 -*-
# @Time : 2022/4/14 15:57
# @Author : DongYun
# @File : HJ28素数伴侣.py
# @Software : PyCharm
from typing import List
import math


def sushu(x):
    num = int(math.sqrt(x)+0.5)
    for i in range(2,num+1):
        if x % i == 0:
            return False
    return True
# print(sushu(9))
def check(odd,list_even,used,match):
    for i in range(len(list_even)):
        if sushu(odd+list_even[i]) and not used[i]:
            used[i] = True
            if match[i] == 0 or check(match[i],list_even,used,match):
                match[i] = odd
                return True
    return False
while True:
    try:
        count = 0
        N = int(input())
        list_ = list(map(int, input().split(" ")))
        list_even,list_odd = [],[]
        for x in list_:
            if x % 2:
                list_odd.append(x)
            else:
                list_even.append(x)
        if len(list_odd) == 0 or len(list_even) == 0:
            print(count)
            continue
        match = [0]*len(list_even)
        for odd in list_odd:
            used = [False]*len(list_even)
            if check(odd,list_even,used,match):
                count+=1
        print(count)
    except:
        break
# 4
# 2 5 6 13