from collections import defaultdict
from typing import List
# class Solution:
#     def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
#         G = defaultdict(list)
#         for u,v in edges:
#             G[u].append(v)
#             G[v].append(u)
#         visited = [False] * (n+1)
#         visited[1] = True
#         def dfs(i,t):
#             length = len(G[i])
#             if i > 1:
#                 length -= 1
#             if length == 0 or t == 0:    # 表示已经走完了
#                 return 1 if i == target else 0
#             visited[i] = True         
#             for j in G[i]:                # 遍历所有的子节点
#                 if not visited[j]:         
#                     ans = dfs(j,t-1)     #
#                     if ans > 0:          # 如果找到了，就返回
#                         return ans / length
#             return 0
#         return dfs(1,t)


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        G = defaultdict(list)
        for u,v in edges:
            G[u].append(v)
            G[v].append(u)
        visited = [False] * (n+1)
        visited[1] = True
        quere = [[1,1.0]]
        while quere and t >= 0:
            for _ in range(len(quere)):
                i,p = quere.pop(0)
                length = len(G[i]) 
                if i > 1:
                    length -= 1
                if length == 0 or t == 0:
                    if i == target:
                        return p
                    else:
                        continue
                for j in G[i]:
                    if not visited[j]:
                        visited[j] = True
                        quere.append([j,p/length])
            t -= 1
        return 0
n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 2
target = 4

# n = 7
# edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
# t = 1
# target = 7
print(Solution().frogPosition(n,edges,t,target))