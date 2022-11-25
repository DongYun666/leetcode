# -*- codeing = utf-8 -*-
# @Time : 2022/3/4 9:30
# @Author : DongYun
# @File : 2104.子数组范围的和.py
# @Software : PyCharm
from typing import List
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for index,num in enumerate(nums):
            res +=  num*(((-1)*(index+len(nums))*(len(nums)-index-1)/2)+(index*(index+1)/2))
        return res
    def subArrayRanges2(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            min_val,max_val = float("inf"),float("-inf")
            for j in range(i,len(nums)):
                min_val = min(min_val,nums[j])
                max_val = max(max_val,nums[j])
                res+=max_val-min_val
        return res

nums=[4,-2,-3,4,1]
print(Solution().subArrayRanges2(nums))