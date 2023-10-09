from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        start,end,count = 0,0,0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
                elif grid[i][j] == 1:
                    count += 1
                    start,end = i,j
        
        def dfs(i,j,c):
            if grid[i][j] == 2:
                return 1 if c == 0 else 0
            temp = grid[i][j]
            grid[i][j] = -1
            res = 0
            for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] in [0,2]:
                    res += dfs(x,y,c - 1)
            grid[i][j] = temp
            return res
        return dfs(start,end,count)
grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# grid = [[1,0],[0,2]]
grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
print(Solution().uniquePathsIII(grid))

                