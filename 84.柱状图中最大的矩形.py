# -*- codeing = utf-8 -*-
# @Time : 2022/4/28 21:01
# @Author : DongYun
# @File : 84.柱状图中最大的矩形.py
# @Software : PyCharm
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        for index,height in enumerate(heights):
            i,j = 0,0
            for i in range(index,-1,-1):
                if heights[i]<height:
                    break
            for j in range(index,len(heights)):
                if heights[j]<height:
                    break
            if i == 0:
                ans = max(ans,height*(j-i+1))
            else:
                ans = max(ans,height*(j-i-1))
        return ans




heights = [2, 1, 5, 6, 2, 3]
print(Solution().largestRectangleArea(heights))


