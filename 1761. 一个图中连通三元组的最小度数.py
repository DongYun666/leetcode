from typing import List
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = [[0] * (n + 1) for _ in range(n + 1)]
        degree = [0] * (n + 1)
        for u, v in edges:
            graph[u][v] = graph[v][u] = 1
            degree[u] += 1
            degree[v] += 1
        ans = float('inf')
        for i in range(1, n + 1):
            for j in range(i + 1,n + 1):
                if graph[i][j] == 1:
                    for k in range(j + 1, n + 1):
                        if graph[i][k] == 1 and graph[j][k] == 1:
                            ans = min(ans, degree[i] + degree[j] + degree[k] - 6)
        return ans if ans != float('inf') else -1
    
n = 6
edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]

n = 7
edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
print(Solution().minTrioDegree(n, edges))