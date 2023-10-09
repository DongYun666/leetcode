from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        quere = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    quere.append((i,j,0))
        time = 0
        while quere:
            i,j,time = quere.pop(0)
            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == 1:
                    grid[x][y] = 2
                    quere.append((x,y,time+1))
        for row in grid:
            if 1 in row:
                return -1
        return time
    
grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[2,1,1],
        [0,1,1],
        [1,0,1]]
print(Solution().orangesRotting(grid))