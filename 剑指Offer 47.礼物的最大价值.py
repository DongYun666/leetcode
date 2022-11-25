# -*- codeing = utf-8 -*-
# @Time : 2022/3/16 16:55
# @Author : DongYun
# @File : 剑指Offer 47.礼物的最大价值.py
# @Software : PyCharm
from typing import List

class Solution:
    def maxValue2(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        def recure(x,y):
            if x >=row or y >= col:
                return 0
            return grid[x][y] + max(recure(x,y+1),recure(x+1,y))
        return recure(0,0)
    def maxValue(self, grid: List[List[int]]) -> int:
        # for i in range(1,len(grid)):
        #     grid[i][0] += grid[i-1][0]
        # for j in range(1,len(grid[0])):
        #     grid[0][j] += grid[0][j-1]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:continue
                elif i == 0 and j!=0: grid[i][j]+=grid[i][j-1]
                elif j == 0 and i!=0: grid[i][j]+=grid[i-1][j]
                else:grid[i][j] += max(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]

grid =[[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(Solution().maxValue(grid))


