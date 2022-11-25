# -*- codeing = utf-8 -*-
# @Time : 2022/7/24 18:54
# @Author : DongYun
# @File : 1186.删除一次得到子数组最大和.py
# @Software : PyCharm
from typing import List
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        arr_sum = sum(arr)
        min_sum = min(arr)
        temp = 0
        if arr_sum>0 and min_sum<=0:
            temp = arr_sum - min_sum
        else:
            temp = arr_sum+min_sum
        return max(max(arr),temp)

arr = [-1,-1,-1,-1]
print(Solution().maximumSum(arr))



