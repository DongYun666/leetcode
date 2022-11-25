# -*- codeing = utf-8 -*-
# @Time : 2022/4/6 9:03
# @Author : DongYun
# @File : 310.最小高度树.py
# @Software : PyCharm
from collections import defaultdict, deque
from typing import List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        parents = [0]*n
        def bfs(start : int ):
            vis = [False]*n
            vis[start] = True
            q = deque([start])
            while q:
                x = q.popleft()
                for y in g[x]:
                    if not vis[y]:
                        vis[y] = True
                        parents[y] = x
                        q.append(y)
            return x
        x = bfs(0)
        y = bfs(x)
        path = []
        parents[x] = -1
        while y != -1:
            path.append(y)
            y = parents[y]
        m = len(path)
        if m%2:
            res = [path[m//2]]
        else:
            res = [path[m//2-1],path[m//2]]
        return res

        print(edges)
        print(g)



n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
print(Solution().findMinHeightTrees(n,edges))



