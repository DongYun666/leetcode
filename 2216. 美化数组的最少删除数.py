# -*- codeing = utf-8 -*-
# @Time : 2022/4/6 20:09
# @Author : DongYun
# @File : 2216. 美化数组的最少删除数.py
# @Software : PyCharm

from typing import  List
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        stack = [nums[0]]
        res = 0
        for i in range(1,len(nums)):
            if len(stack) % 2:
                if nums[i] != stack[-1]:
                    stack.append(nums[i])
                else:
                    res +=1
            else:
                stack.append(nums[i])
        return res+len(stack)%2

nums = [1,1,2,2,3,3]
print(Solution().minDeletion(nums))