# -*- codeing = utf-8 -*-
# @Time : 2022/4/4 20:03
# @Author : DongYun
# @File : 5219.每个小孩最多能分到多少苹果.py
# @Software : PyCharm

from typing import List
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        candies_sum = sum(candies)
        if k > candies_sum:
            return 0
        left , right = 1 , candies_sum // k
        res = 0
        def check(num : int):
            temp = k
            for candie in candies:
                if candie < num :
                    continue   # 表示不能分
                temp -= candie // num
            return temp <=0
        while left <= right:
            mid = (left + right) //2
            if check(mid):
               res = mid
               left = mid +1
            else :
                right = mid -1
        return res

candies = [5,8,6]
k = 3
print(Solution().maximumCandies(candies,k))