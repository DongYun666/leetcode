from typing import List
class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        # 收集初始状态时的火的位置
        fires = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fires.append((i,j))
        #让火烧一轮
        fire_visted = [[float("inf")] * n for _ in range(m)]
        step = 0
        while fires:
            temp = fires
            fires = []
            for i,j in temp:
                fire_visted[i][j] = step
                for nx,ny in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny] != 2 and fire_visted[nx][ny] == float("inf"):
                        fires.append((nx,ny))
            step += 1
        # 让人开始走
        people = [(0,0,fire_visted[0][0])]
        people_visted = [[False] * n for _ in range(m)]
        people_visted[0][0] = True
        step = 1
        res = 0
        while people:
            temp = people
            people = []
            for i,j,fire_step in temp:
                for nx,ny in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny] != 2 and not people_visted[nx][ny]:
                        if nx == m-1 and ny == n-1: 
                            res = max(res,min(fire_step,fire_visted[nx][ny] - step + 1))
                        elif fire_visted[nx][ny] > step: 
                            people.append((nx,ny,min(fire_visted[nx][ny]-step,fire_step)))
                            people_visted[nx][ny] = True
            step += 1
        return res-1 if res != float("inf") else 10**9
    
grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]

grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]]

grid = [[0,0,0],[2,2,0],[1,2,0]]
print(Solution().maximumMinutes(grid))
