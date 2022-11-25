# -*- codeing = utf-8 -*-
# @Time : 2022/5/2 19:27
# @Author : DongYun
# @File : 179.最大数.py
# @Software : PyCharm
from functools import cmp_to_key
from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = []
        for num in nums:
            nums_str.append(str(num))
        def Quick_Sort(nums_str,begin,end):
            if begin>end:
                return
            left,right = begin,end
            temp = nums_str[begin]
            while left!=right:
                while nums_str[right]+temp<=temp+nums_str[right] and left<right:
                    right-=1
                while nums_str[left]+temp>=temp+nums_str[left] and left<right:
                    left+=1
                if left<right:
                    nums_str[left],nums_str[right] = nums_str[right],nums_str[left]
            nums_str[begin] = nums_str[left]
            nums_str[left] = temp
            Quick_Sort(nums_str,begin,left-1)
            Quick_Sort(nums_str,left+1,end)
        Quick_Sort(nums_str,0,len(nums_str)-1)
        return "".join(nums_str) if nums_str[0]!="0" else "0"

nums = [3, 30, 34, 5, 9]
print(Solution().largestNumber(nums))

