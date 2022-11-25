from collections import defaultdict
from typing import List

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        res = 0
        dict = defaultdict(list)
        for x,y in roads:
            dict[x].append(y)
            dict[y].append(x)
        def dfs(x,fa):
            size = 1
            for y in dict[x]:
                if y!= fa:
                    size += dfs(y,x)
            if x:
                nonlocal res
                res +=(size + seats -1)//seats
            return size
        dfs(0,-1)
        return res

roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]
seats = 2
print(Solution().minimumFuelCost(roads, seats))