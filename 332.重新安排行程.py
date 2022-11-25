# -*- codeing = utf-8 -*-
# @Time : 2021/12/4 15:25
# @Author : DongYun
# @File : 332.重新安排行程.py
# @Software : PyCharm
from collections import Counter
from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets_len = [1]*len(tickets)
        print(tickets_len)
        return ['','','']

print(Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))