import collections
import heapq
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # 构建邻接表
        gruph = collections.defaultdict(list)
        for i, (a, b) in enumerate(edges):
            gruph[a].append((succProb[i],b))
            gruph[b].append((succProb[i],a))
        que = [(-1.0,start)]
        prob = [0.0] * n
        prob[start] = 1.0
        while que:
            p, node = heapq.heappop(que)
            p = -p
            if p < prob[node]:
                continue
            for next_p,next_node  in gruph[node]:
                if prob[next_node] < prob[node] * next_p:
                    prob[next_node] = prob[node] * next_p
                    heapq.heappush(que, (-prob[next_node], next_node))
        return prob[end]
    
n = 3
edges = [[0,1]]
succProb = [0.5]
start = 0
end = 2

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2

print(Solution().maxProbability(n, edges, succProb, start, end))