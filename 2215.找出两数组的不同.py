# -*- codeing = utf-8 -*-
# @Time : 2022/4/6 19:42
# @Author : DongYun
# @File : 2215.找出两数组的不同.py
# @Software : PyCharm

from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        res = [[],[]]
        for num in nums1:
            if num not in nums2:
                res[0].append(num)
        for num in nums2:
            if num not in nums1:
                res[1].append(num)
        return res

nums1 = [1,2,3,3]
nums2 = [1,1,2,2,4,6]
print(Solution().findDifference(nums1,nums2))