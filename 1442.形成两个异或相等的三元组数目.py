# -*- codeing = utf-8 -*-
# @Time : 2022/7/29 17:21
# @Author : DongYun
# @File : 1442.形成两个异或相等的三元组数目.py
# @Software : PyCharm
import functools
import itertools
from collections import defaultdict
from typing import List
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        dict_temp = defaultdict(int)
        if len(arr)<3:
            return 0
        for i in range(len(arr)-2):
            x = arr[i]
            for j in range(i+1,len(arr)):
                x^=arr[j]
                for k in range(j,len(arr)-2):














arr = [2, 3, 1, 6, 7]
print(Solution().countTriplets(arr))




