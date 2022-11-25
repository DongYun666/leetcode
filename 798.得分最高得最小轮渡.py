# -*- codeing = utf-8 -*-
# @Time : 2022/7/21 15:47
# @Author : DongYun
# @File : 798.得分最高得最小轮渡.py
# @Software : PyCharm
from typing import List
class Solution:
    def check(self,nums_list:List[int]):
        count = 0
        for index,x in enumerate(nums_list):
            if x<=index:
                count+=1
        return count
    def bestRotation(self, nums: List[int]) -> int:
        res = 0
        max_score = -1
        temp = []
        for i in range(len(nums)):
            temp.append(nums[i:]+nums[:i])
        for index,x in enumerate(temp):
            score = self.check(x)
            if score>max_score:
                max_score = score
                res = index
        return res


nums = [1,3,0,2,4]
print(Solution().bestRotation(nums))
