# -*- codeing = utf-8 -*-
# @Time : 2022/4/27 19:35
# @Author : DongYun
# @File : 64.最小路径和.py
# @Software : PyCharm
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j != 0:
                    grid[i][j] = grid[i][j]+grid[i][j-1]
                elif j == 0 and i!= 0:
                    grid[i][j] = grid[i-1][j]+grid[i-1][j]
                elif i != 0 and j != 0:
                    grid[i][j] = min(grid[i-1][j]+grid[i][j],grid[i][j-1]+grid[i][j])
        return grid[-1][-1]

grid = [[0,1],[1,0]]
print(Solution().minPathSum(grid))