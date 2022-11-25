# -*- codeing = utf-8 -*-
# @Time : 2022/4/24 17:31
# @Author : DongYun
# @File : 6041.多个数组求交集.py
# @Software : PyCharm
from collections import Counter
from typing import List
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        c = Counter(nums[0])
        res = []
        for num in nums[1:]:
            c+=Counter(num)
        for key,value in c.items():
            if value == len(nums):
                res.append(key)
        return sorted(res)
nums = [[1,2,3],[4,5,6]]
print(Solution().intersection(nums))
