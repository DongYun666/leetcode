from heapq import heappop, heappush
from typing import List
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pairs = sorted(zip(quality,wage), key=lambda p:p[1]/p[0])
        ans = float("inf")
        total = 0
        h = []
        for q,w in pairs[:k-1]:
            total +=q
            heappush(h,-q)
        for q,w in pairs[k-1:]:
            total += q
            heappush(h,-q)
            ans = min(ans,w/q * total)
            total += heappop(h)
        return ans,total





quality = [3,1,10,10,1]
wage = [4,8,2,2,7]
k = 3
print(Solution().mincostToHireWorkers(quality,wage,k))