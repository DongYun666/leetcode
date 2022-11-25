# -*- codeing = utf-8 -*-
# @Time : 2022/2/19 16:40
# @Author : DongYun
# @File : 179.最大整数.py
# @Software : PyCharm
import functools
from typing import List
class Solution(object):
    def largestNumber(self, nums):
        nums_str = list(map(str, nums))
        compare = lambda x,y: 1 if x+y < y+x else -1
        nums_str.sort(key=functools.cmp_to_key(compare))
        res = "".join(nums_str)
        if res[0] == "0":
            res = "0"
        return res


nums = [3,30,34,5,9]
print(Solution().largestNumber(nums))