# # -*- codeing = utf-8 -*-
# # @Time : 2021/12/7 8:44
# # @Author : DongYun
# # @File : 1034.边界着色.py
# # @Software : PyCharm
# from typing import List
#
# class Solution:
#     def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
#         temp = grid[row][col]
#
#         def dfs(row,col):
#             if row+1 >= len(grid):
#                 return
#             if col+1 >= len(grid[0]):
#                 return
#             if grid[row+1][col] != temp or grid[row][col+1] != temp or grid[row-1][col] != temp or grid[row][col-1] != temp:
#                 grid[row][col] = color
#             else:
#                 dfs(row+1,col)
#                 dfs(row,col+1)
#                 dfs(row-1,col)
#                 dfs(row,col-1)
#         dfs(row,col)
#
#         return grid
#
#
# print(Solution().colorBorder([[1,1],[1,2]],0,0,3))
#
#
#
#
from typing import List

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        borders = []
        originalColor = grid[row][col]
        visited[row][col] = True
        self.dfs(grid, row, col, visited, borders, originalColor)
        for x, y in borders:
            grid[x][y] = color
        return grid

    def dfs(self, grid, x, y, visited, borders, originalColor):
        isBorder = False
        m, n = len(grid), len(grid[0])
        direc = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for dx, dy in direc:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == originalColor):
                isBorder = True
            elif not visited[nx][ny]:
                visited[nx][ny] = True
                self.dfs(grid, nx, ny, visited, borders, originalColor)
        if isBorder:
            borders.append((x, y))


print(Solution().colorBorder([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]],1,1,2))


