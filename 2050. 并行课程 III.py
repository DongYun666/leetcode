from collections import defaultdict
from typing import List

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # 构建邻接表 和 入度表
        adj = defaultdict(list)
        indegree = [0] * (n)
        for u, v in relations:
            adj[u-1].append(v-1)
            indegree[v-1] += 1
        q = []
        f = [0] * n
        res = 0
        for i, v in enumerate(indegree):
            if v == 0:
                q.append(i)
                f[i] = time[i]
                res = max(res, f[i])
        while q:
            u = q.pop(0)
            for v in adj[u]:
                indegree[v] -= 1
                f[v] = max(f[v], f[u] + time[v])
                res = max(res, f[v])
                if indegree[v] == 0:
                    q.append(v)
        return res
    

