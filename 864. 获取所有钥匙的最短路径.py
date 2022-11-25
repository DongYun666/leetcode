from collections import defaultdict
from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        start_x,start_y,cnt = 0,0,0
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    start_x = i
                    start_y = j
                elif grid[i][j].islower():
                    cnt+=1
        q = [[start_x,start_y,0]]
        dict = defaultdict(lambda :0x3f3f3f3f)
        dict[(start_x,start_y,0)] = 0
        while len(q)!=0:
            x,y,mark = q.pop(0)
            step = dict[(x,y,mark)]
            for dx,dy in dirs:
                new_x = x+dx   #四个方向
                new_y = y+dy
                if 0<=new_x<m and 0<=new_y<n and grid[new_x][new_y]!="#":                     #   排除#号
                    c = grid[new_x][new_y]
                    if c.isupper() and (mark>>(ord(c)-ord("A")) & 1) == 0:  #大写 不存在钥匙直接进行下一步
                        continue
                    new_mark = mark
                    if c.islower():
                        new_mark |= (1<<(ord(c)-ord("a")))
                    if new_mark == (1<<cnt)-1:   #达到钥匙数
                        return step+1
                    if step+1>=dict[(new_x,new_y,new_mark)]:
                        continue
                    dict[(new_x,new_y,new_mark)] = step+1
                    q.append([new_x,new_y,new_mark])
        return -1

grid = ["@..aA", "..B#.", "....b"]
grid = ["@.a.#","###.#","b.A.B"]
grid = ["@Aa"]
print(Solution().shortestPathAllKeys(grid))