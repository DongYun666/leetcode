from functools import lru_cache
from typing import List
class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m,n = len(grid),len(grid[0])
        if (m+n) % 2 == 0 or grid[0][0] == ")" or grid[-1][-1] == "(":return False
        @lru_cache(None)
        def dfs(x,y,l,r):
            if x >= m or y >= n or l < r or l-r > m-x+n-y-1:
                return False
            if grid[x][y] == "(":
                l += 1
            else:
                r += 1
            if x == m-1 and y == n-1 and l == r:
                return True
            return dfs(x+1,y,l,r) or dfs(x,y+1,l,r)
        return dfs(0,0,0,0)
grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
grid = [[")",")"],["(","("]]
print(Solution().hasValidPath(grid))
