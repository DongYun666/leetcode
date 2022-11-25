# -*- codeing = utf-8 -*-
# @Time : 2022/7/29 13:43
# @Author : DongYun
# @File : 599.两个列表的最小索引总和.py
# @Software : PyCharm
from collections import defaultdict
from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index = {s: i for i, s in enumerate(list1)}
        ans = []
        indexSum = float("inf")
        for i, s in enumerate(list2):
            if s in index:
                j = index[s]
                if i + j < indexSum:
                    indexSum = i + j
                    ans = [s]
                elif i + j == indexSum:
                    ans.append(s)
        return ans




list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines","Hungry Hunter Steakhouse", "Shogun"]
print(Solution().findRestaurant(list1,list2))
