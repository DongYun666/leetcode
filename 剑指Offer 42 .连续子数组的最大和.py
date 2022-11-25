# -*- codeing = utf-8 -*-
# @Time : 2022/3/16 16:17
# @Author : DongYun
# @File : 剑指Offer 42 .连续子数组的最大和.py
# @Software : PyCharm
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                res = max(res, sum(nums[i:j + 1]))
        return res

    def maxSubArray1(self, nums: List[int]) -> int:
        max_num = float("-inf")
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
                max_num = max(max_num, nums[i])
        return max_num


nums = [1, 2]
print(Solution().maxSubArray1(nums))
