# -*- codeing = utf-8 -*-
# @Time : 2022/3/7 11:42
# @Author : DongYun
# @File : 剑指Offer 53.在排序数组中查找数字.py
# @Software : PyCharm
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = 0
        for num in nums:
            if num == target and num <=target:
                count+=1
        return count

nums = [5,7,7,8,8,10]
target = 8
print(Solution().search(nums,target))