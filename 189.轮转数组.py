# -*- codeing = utf-8 -*-
# @Time : 2022/5/2 20:59
# @Author : DongYun
# @File : 189.轮转数组.py
# @Software : PyCharm

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums = nums[(len(nums)-k):].copy() + nums[:len(nums)-k].copy()
        print(nums)
nums = [1,2,3,4,5,6,7]
k = 3
print(Solution().rotate(nums,k))
# 快速排序
nums.sort()
# 快速排序
