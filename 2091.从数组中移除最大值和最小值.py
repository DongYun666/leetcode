# -*- codeing = utf-8 -*-
# @Time : 2021/12/3 20:13
# @Author : DongYun
# @File : 2091..py
# @Software : PyCharm
from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_index,max_index,minnum,maxnum = 0,0,nums[0],nums[0]
        for index,num in  enumerate(nums):
            if num<minnum:
                minnum = num
                min_index = index
            if num>maxnum:
                max_index = index
        l = min(min_index,max_index)
        r = max(min_index,max_index)
        n = len(nums)
        return min(r+1,n-l,l+1+n-r)

print(Solution().minimumDeletions([2,10,7,5,4,1,8,6]))


