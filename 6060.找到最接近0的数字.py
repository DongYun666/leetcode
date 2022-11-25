# -*- codeing = utf-8 -*-
# @Time : 2022/4/17 18:36
# @Author : DongYun
# @File : 6060.找到最接近0的数字.py
# @Software : PyCharm

from typing import List
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = nums[0]
        min_dis = abs(res)
        for num in nums:
            if abs(res) == abs(num):
                res=max(res,num)
            elif abs(num)<min_dis:
                min_dis = abs(num)
                res = num

        return res

nums = [-4,-2,1,-1,4,8]
print(Solution().findClosestNumber(nums))