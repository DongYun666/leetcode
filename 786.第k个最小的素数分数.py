# -*- codeing = utf-8 -*-
# @Time : 2021/11/29 19:14
# @Author : DongYun
# @File : 786.第k个最小的素数分数.py
# @Software : PyCharm
from functools import cmp_to_key
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        def my_sort(x,y):
            return -1 if x[0]*y[1]<x[1]*y[0] else 1
        temp = []
        for index,i in enumerate(arr):
            for j in arr[:index:-1]:
                temp.append((i,j))
        temp.sort(key=cmp_to_key(my_sort))
        print(temp)
        return list(temp[k-1])


print(Solution().kthSmallestPrimeFraction([1,2,3,5,7],3))