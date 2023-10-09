from typing import List
class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        #构建图
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append([edge[1],edge[2]])
            graph[edge[1]].append([edge[0],edge[2]])
        # print(graph)
        # 构建最短路径 从source到 destination 的最短距离为 target
        import heapq
        heap = []
        heapq.heappush(heap,[0,source])
        visited = [False] * n
        while heap:
            # print(heap)
            dis,cur = heapq.heappop(heap)
            if cur == target:
                break
            if visited[cur]:
                continue
            visited[cur] = True
            for next in graph[cur]:
                if visited[next[0]]:
                    continue
                heapq.heappush(heap,[dis + next[1],next[0]])
        # print(dis)
