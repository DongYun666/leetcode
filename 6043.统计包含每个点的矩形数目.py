# -*- codeing = utf-8 -*-
# @Time : 2022/4/24 18:38
# @Author : DongYun
# @File : 6043.统计包含每个点的矩形数目.py
# @Software : PyCharm

from typing import List
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        res = []
        rectangles = sorted(rectangles,key= lambda x:-x[0])
        for x,y in points:
            count = 0
            left,right = 0,len(rectangles)-1
            while left<=right:
                mid = (left+right) // 2
                if x < rectangles[mid][0]:
                    left = mid+1
                elif x == rectangles[mid][0]:
                    left = mid+1
                else:
                    right = mid-1
            temp = sorted(rectangles[0:left],key=lambda x:-x[1])
            left, right = 0, len(temp) - 1
            while left<=right:
                mid = (left+right) // 2
                if y < temp[mid][1]:
                    left = mid+1
                elif y == temp[mid][1]:
                    left=mid+1
                else:
                    right = mid-1
            res.append(left)
        return res


rectangles = [[1,1],[2,2],[3,3]]
points = [[1,3],[1,1]]
print(Solution().countRectangles(rectangles,points))