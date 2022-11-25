# -*- codeing = utf-8 -*-
# @Time : 2022/2/20 11:18
# @Author : DongYun
# @File : 1394.找出数组中的幸运数字.py
# @Software : PyCharm
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        num_count,ans = {},-1
        for num in arr:
            num_count[num] = num_count.get(num,0)+1
        for key,value in num_count.items():
            if key == value:
                ans = max(ans,key)
        return ans

arr = [1,2,2,3,3]
print(Solution().findLucky(arr))
