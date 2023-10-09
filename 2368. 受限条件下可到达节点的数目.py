from typing import List

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        from collections import defaultdict
        graph = defaultdict(list)
        for u,v in edges:
            if u not in restricted and v not in restricted:
                graph[u].append(v)
                graph[v].append(u)
        res = 1
        visited = [0]
        queue = [0]
        while queue:
            node = queue.pop(0)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    res += 1
                    visited.append(neighbor)
                    queue.append(neighbor)
        return res
    
n = 7
edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
restricted = [4,5]

n = 7
edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]]
restricted = [4,2,1]

print(Solution().reachableNodes(n, edges, restricted))