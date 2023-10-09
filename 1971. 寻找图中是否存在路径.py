from collections import defaultdict
from typing import List

class Solution:
    # 并查集
    def validPath1(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        fa = list(range(n))
        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        def merge(x,y):
            fa[find(x)] = find(y)

        for x,y in edges:
            merge(x,y)
        return find(source) == find(destination)

    # DFS
    def validPath_DFS(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = [False] * n
        adjacent = defaultdict(list)
        for x,y in edges:
            adjacent[x].append(y)
            adjacent[y].append(x)
        def dfs(source,destination):
            if source == destination:
                return True
            visited[source] = True
            for next in adjacent[source]:
                if not visited[next] and dfs(next,destination):
                    return True
            return False
        return dfs(source,destination)

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = [False] * n
        adjacent = defaultdict(list)
        for x, y in edges:
            adjacent[x].append(y)
            adjacent[y].append(x)
        queries = [source]
        visited[source] == True
        while queries:
            temp = queries.pop()
            if temp == destination:
                break
            for next in adjacent[temp]:
                if not visited[next]:
                    queries.append(next)
                    visited[next] = True
        return visited[destination]


n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2
print(Solution().validPath(n, edges, source, destination))