from functools import cache
from typing import List
class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        @cache
        def dfs(i,j,d):
            if 0<=i+d<m and 0<= j+d < n:
                return dfs(i+d,j+d,d) | {grid[i+d][j+d]}
            else:
                return set()
        return [[abs(len(dfs(i,j,1)) - len(dfs(i,j,-1))) for j in range(n)] for i in range(m)]
grid = [[1,2,3],[3,1,5],[3,2,1]]
grid = [[1,2,3],[3,1,5],[3,2,1]]
print(Solution().differenceOfDistinctValues(grid))
