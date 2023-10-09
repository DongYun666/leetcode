from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visted = [[False] * len(grid[0]) for _ in range(len(grid))]
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        if len(grid) == 1 and len(grid[0]) == 1: return 1
        quere = [(0,0)]
        visted[0][0] = True
        step = 1
        while quere:
            temp = quere
            quere = []
            for i,j in temp:
                for nx,ny in [(i,j+1),(i+1,j),(i+1,j+1),(i-1,j),(i,j-1),(i-1,j-1),(i-1,j+1),(i+1,j-1)]:
                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and not visted[nx][ny] and grid[nx][ny] == 0:
                        if nx == len(grid)-1 and ny == len(grid[0])-1: return step+1
                        quere.append((nx,ny))
                        visted[nx][ny] = True
            step += 1
        return -1
grid = [[0,0,0],[1,1,0],[1,1,0]]
print(Solution().shortestPathBinaryMatrix(grid))