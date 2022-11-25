# -*- codeing = utf-8 -*-
# @Time : 2022/7/10 10:20
# @Author : DongYun
# @File : 第一题.py
# @Software : PyCharm
from typing import List
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort(reverse=True)
        count = 0
        while sum(amount):
            count+=1
            if amount[0]!=0:
                amount[0]-=1
            if amount[1]!=0:
                amount[1]-=1
            amount.sort(reverse=True)
        return count


amount = [5, 4, 4]
print(Solution().fillCups(amount))