import heapq
from typing import List
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m,n = len(grid),len(grid[0])
        res = [0] * len(queries)
        query = [(grid[0][0],0,0)]
        grid[0][0] = 0
        cnt = 0
        for index,q in sorted(enumerate(queries),key=lambda x:x[1]):
            while query and query[0][0] < q:
                cnt += 1
                val,i,j = heapq.heappop(query)
                for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=x<m and 0<=y<n and grid[x][y]:
                        heapq.heappush(query,(grid[x][y],x,y))
                        grid[x][y] = 0
            res[index] = cnt
        return res
grid = [[1,1,1],[2,2,2],[3,3,3]]
queries = [2,2,2]

grid = [[1,2,3],[2,5,7],[3,5,1]]
queries = [5,6,2]
print(Solution().maxPoints(grid,queries))