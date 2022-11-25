from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j,flag):
            grid[i][j] = 1
            if i == 0 or i == len(grid)-1 or j == 0 or j == len(grid[0])-1:
                return False
            for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
                n_i,n_j = i+x,j+y
                if 0<= n_i <=len(grid) and 0<= n_j <=len(grid[0]) and grid[n_i][n_j] == 0:
                    flag = dfs(n_i,n_j,flag)
            return flag


        res = 0
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                if grid[i][j] == 0 and dfs(i,j,True):
                    res+=1
        return res




grid = [[1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]]
grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
grid = [[1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]]
grid = [[1,1,0,1,1,1,1,1,1,1],
        [0,0,1,0,0,1,0,1,1,1],
        [1,0,1,0,0,0,1,0,1,0],
        [1,1,1,1,1,0,0,1,0,0],
        [1,0,1,0,1,1,1,1,1,0],
        [0,0,0,0,1,1,0,0,0,0],
        [1,0,1,0,0,0,0,1,1,0],
        [1,1,0,0,1,1,0,0,0,0],
        [0,0,0,1,1,0,1,1,1,0],
        [1,1,0,1,0,1,0,0,1,0]]


print(Solution().closedIsland(grid))