# -*- codeing = utf-8 -*-
# @Time : 2022/2/26 14:07
# @Author : DongYun
# @File : 1482.制作m束花所需的最少天数.py
# @Software : PyCharm

from typing import List
class Solution:

    def canMake(self,bloomDay: List[int], day:int,m:int,k:int):
        cur,bouquets = 0,0
        for bloom in bloomDay:
            if bloom <= day:
                cur+=1
                if cur == k:
                    bouquets+=1
                    if bouquets == m:
                        break
                    cur = 0
            else:
                cur = 0
        return bouquets == m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        day_l = min(bloomDay)
        day_r = max(bloomDay)
        while day_l < day_r:
            mid = (day_l+day_r) //2
            if self.canMake(bloomDay, mid,m,k):
                day_r = mid
            else:
                day_l = mid+1
        return day_l

bloomDay = [1,10,3,10,2]
m = 3
k = 1
print(Solution().minDays(bloomDay,m,k))

