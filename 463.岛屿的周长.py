from typing import List

from pip._internal.cache import Cache


class Solution:
    def islandPerimeter2(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        def dfs(i,j):
            if i<0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 1
            if grid[i][j] == 0:
                return 1
            if grid[i][j] != 1:
                return 0
            grid[i][j] = 2
            res = 0
            for l,r in directions:
                new_i = i+l
                new_j = j+r
                res += dfs(new_i,new_j)
            return res

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i,j)

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        load = 0
        bound = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    load+=1
                    if i>0 and grid[i-1][j] == 1:
                        bound+=1
                    if j>0 and grid[i][j-1] == 1:
                        bound+=1
        return 4*load-2*bound







grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
# grid = [[1,1]]
print(Solution().islandPerimeter(grid))
