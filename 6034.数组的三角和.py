# -*- codeing = utf-8 -*-
# @Time : 2022/4/5 19:56
# @Author : DongYun
# @File : 6034.数组的三角和.py
# @Software : PyCharm

from typing import List
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for i in range(len(nums)-1,-1,-1):
            for j in range(0,i):
                nums[j] += nums[j+1]
                nums[j] %= 10
        return nums[0]

nums =[1,2,3,4,5]
print(Solution().triangularSum(nums))
