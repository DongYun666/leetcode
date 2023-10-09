import bisect
from collections import defaultdict
from typing import List

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        # 1. 统计每个点的度数
        degree = [0] * n
        same_degree = defaultdict(int)
        for edge in edges:
            x,y = edge[0] - 1,edge[1] - 1
            if x > y:
                x,y = y,x
            degree[x] += 1
            degree[y] += 1
            same_degree[x * n + y] += 1

        # 使用二分查找
        temp = sorted(degree)
        res = []
        for query in queries:
            total = 0
            for i in range(n):
                j = bisect.bisect_right(temp, query - temp[i],i + 1)
                total += n - j
            for val,freq in same_degree.items():
                x,y = val // n, val % n
                if degree[x] + degree[y] > query and degree[x] + degree[y] - freq <= query:
                    total -= 1
            res.append(total)
        return res


n = 5
edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]]
queries = [1,2,3,4,5]
print(Solution().countPairs(n, edges, queries))