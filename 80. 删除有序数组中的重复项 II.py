# -*- codeing = utf-8 -*-
# @Time : 2022/4/28 19:12
# @Author : DongYun
# @File : 80. 删除有序数组中的重复项 II.py
# @Software : PyCharm
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<3:
            return len(nums)
        p,q = 2,2
        while q < len(nums):
            if nums[p-2]!= nums[q]:
                nums[p] = nums[q]
                p+=1
            q+=1
        return p



nums = [0,0,0,0,0,1,1,1,1,2,3,3]
print(Solution().removeDuplicates(nums))