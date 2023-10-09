from typing import List
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        from  collections import defaultdict
        dict = defaultdict(list)
        for edge in edges:
            dict[edge[0]].append(edge[1])
            dict[edge[1]].append(edge[0])
        visited = [False] * n
        def dfs(node):
            visited[node] = True
            vnum,enum = 1,len(dict[node])
            for neighbor in dict[node]:
                if not visited[neighbor]:
                    v,e = dfs(neighbor)
                    vnum += v
                    enum += e
            return vnum,enum
        res = 0
        for i in range(n):
            if not visited[i]:
                v,e = dfs(i)
                if e == v * (v-1):
                    res += 1
        return res
    
n = 6
edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
# edges = [[0,1],[0,2],[1,2],[3,4]]
print(Solution().countCompleteComponents(n, edges)) # 2