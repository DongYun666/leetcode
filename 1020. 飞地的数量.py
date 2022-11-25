from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])

        def dfs(i,j):
            if i<0 or i>=n or j<0 or j>=m or grid[i][j] == 0:
                return
            grid[i][j] = 0
            for a,b in [[1,0],[-1,0],[0,1],[0,-1]]:
                dfs(a+i,b+j)
        for i in range(n):
            if grid[i][0]==1:
                dfs(i,0)
            if grid[i][m-1]==1:
                dfs(i,m-1)
        for j in range(m):
            if grid[0][j] == 1:
                dfs(0,j)
            if grid[n-1][j] == 1:
                dfs(n-1,j)
        return sum(sum(t) for t in grid)




grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
print(Solution().numEnclaves(grid))