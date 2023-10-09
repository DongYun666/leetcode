from typing import List
class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:

        def bfs(i,j):
            query = [(i,j)]
            ans = 1
            while query:
                x,y = query.pop(0)
                land[x][y] = 1
                for dx,dy in [[0,1],[0,-1],[1,0],[1,1],[1,-1],[-1,0],[-1,1],[-1,-1]]:
                    if 0<=x+dx<len(land) and 0<=y + dy <len(land[0]) and land[x + dx][y+dy] == 0:
                        query.append((x+dx,y+dy))
                        ans += 1
            return ans
        res = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 0:
                    res.append(bfs(i,j))
        return sorted(res)
    
land = [
        [0,2,1,0],
        [0,1,0,1],
        [1,1,0,1],
        [0,1,0,1]
        ]
print(Solution().pondSizes(land))