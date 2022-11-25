# -*- codeing = utf-8 -*-
# @Time : 2022/4/28 19:46
# @Author : DongYun
# @File : 81.搜索旋转排序数组 II.py
# @Software : PyCharm

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for num in nums:
            if num < target:
                continue
            if num == target:
                return True
            if num > target:
                break
        for num in nums[::-1]:
            if num > target:
                continue
            if num == target:
                return True
            if num < target:
                break
        return False


nums = [2,5,6,0,0,1,2]
target = 3
print(Solution().search(nums,target))