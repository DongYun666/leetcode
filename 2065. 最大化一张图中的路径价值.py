from collections import defaultdict
from typing import List

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        d = defaultdict(list)
        for x,y,z in edges:
            d[x].append([y,z])
            d[y].append([x,z])
        visted = [0]
        ans = 0
        def dfs(cur,t,value):
            if cur == 0:
                nonlocal ans
                ans = max(ans, value)
            for v,dist in d[cur]:
                if t+dist<=maxTime:
                    if v not in visted:
                        visted.append(v)
                        dfs(v,t+dist,value+values[v])
                        visted.remove(v)
                    else:
                        dfs(v,t+dist,value)
        dfs(0,0,values[0])
        return ans



values = [0, 32, 10, 43]
edges = [[0, 1, 10], [1, 2, 15], [0, 3, 10]]
maxTime = 49
print(Solution().maximalPathQuality(values, edges, maxTime))