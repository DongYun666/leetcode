from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        def dfs(i,j):
            if i<0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            grid[i][j] = 0
            ans = 1
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_i,new_j = i+x,j+y
                if 0<=new_i<len(grid)and 0<=new_j<len(grid[0]) and grid[new_i][new_j] == 1:
                    ans+=dfs(new_i,new_j)
            return ans

        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if grid[a][b] == 1:
                    res = max(res,dfs(a,b))
        return res


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
grid = [[0,0,0,0,0,0,0,0]]
print(Solution().maxAreaOfIsland(grid))