# -*- codeing = utf-8 -*-
# @Time : 2022/3/7 11:34
# @Author : DongYun
# @File : 剑指Offer 3.数组中重复的数字.py
# @Software : PyCharm
from typing import List
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        temp = [0]*(max(nums)+1)
        for num in nums:
            temp[num]+=1
        for index,count in enumerate(temp):
            if count >=2:
                return index



nums = [2,3,1,0,2,5,3]
print((Solution().findRepeatNumber(nums)))
