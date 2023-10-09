import math
from typing import List
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # 使用大顶堆
        import heapq
        temp = []
        for gift in gifts:
            heapq.heappush(temp, -gift)
        for i in range(k):
            heapq.heappush(temp, -int(math.sqrt(-heapq.heappop(temp))))
        return -sum(temp)
gifts = [25,64,9,4,100]
k = 4

print(Solution().pickGifts(gifts, k))    
