# -*- codeing = utf-8 -*-
# @Time : 2022/4/24 17:50
# @Author : DongYun
# @File : 6042.统计园内格点数目.py
# @Software : PyCharm

from typing import List
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        temp = set()
        count = 0
        max_x,min_x,min_y,max_y = 0,0,0,0
        for circle in circles:
            max_x= max(max_x,circle[0]+circle[2])
            max_y= max(max_y,circle[1]+circle[2])
            min_x= min(min_x,circle[0]+circle[2])
            min_y= min(min_y,circle[1]+circle[2])
        for x in range(min_x,max_x+1):
            for y in range(min_y,max_y+1):
                count+=any((x-a)**2+(y-b)**2<=r**2 for a,b,r in circles )
        return count

circles = [[2,2,2],[3,4,1]]
print(Solution().countLatticePoints(circles))

