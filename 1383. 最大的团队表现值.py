import heapq
from typing import List
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        speed_eff = zip(speed,efficiency)
        speed_eff = sorted(speed_eff,key=lambda x:x[1],reverse=True)
        total = 0
        res = 0 
        stack = []
        for sp,ef in speed_eff:
            total += sp
            res = max(res,total*ef)
            heapq.heappush(stack,sp)
            if len(stack) == k:
                total -= heapq.heappop(stack)
        return res % (10**9 + 7)
    

n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2
print(Solution().maxPerformance(n,speed,efficiency,k))