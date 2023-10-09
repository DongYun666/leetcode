from functools import cache, lru_cache
from typing import List
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        @cache
        def dfs(i,j):
            if i == m-1 and j == n-1:
                return 0
            res = 0
            for x,y in [(i-1,j+1),(i,j+1),(i+1,j+1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] > grid[i][j]:
                    res = max(res,dfs(x,y) + 1)
            return res
        ans = 0
        for i in range(m):
            ans = max(ans,dfs(i,0))
        return ans
    
grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
grid = [[3,2,4],[2,1,9],[1,1,7]]
print(Solution().maxMoves(grid))