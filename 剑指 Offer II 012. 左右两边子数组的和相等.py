# -*- codeing = utf-8 -*-
# @Time : 2022/3/6 19:39
# @Author : DongYun
# @File : 剑指 Offer II 012. 左右两边子数组的和相等.py
# @Software : PyCharm
from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        presum, sum_num = 0, sum(nums)
        for i, num in enumerate(nums):
            if presum == sum_num - num - presum:
                return i
            presum += num
        return -1

nums = [2,1,-1]
print(Solution().pivotIndex(nums))

