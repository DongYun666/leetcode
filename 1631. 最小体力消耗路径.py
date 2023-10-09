import heapq
from typing import List
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n,m = len(heights),len(heights[0])
        res = float('inf')
        query = [(0,0,0)]
        visited = [[False] * m for _ in range(n)]
        while query:
            now,x,y = heapq.heappop(query)
            if visited[x][y]:
                continue
            visited[x][y] = True
            if x == n - 1 and y == m - 1:
                return now
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx,ny = x + dx,y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    heapq.heappush(query,(max(now, abs(heights[nx][ny] - heights[x][y])),nx,ny))
        return res
    
heights = [[1,2,2],[3,8,2],[5,3,5]]
print(Solution().minimumEffortPath(heights))