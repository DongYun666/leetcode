import heapq
from typing import List
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        res = 1
        heapq.heapify(nums)
        while k:
            k-=1
            heapq.heappush(nums,heapq.heappop(nums)+1)
        for n in nums:
            res *= n
            res %= (10**9 + 7)
        return res



nums = [6, 3, 3, 2]
k = 2
print(Solution().maximumProduct(nums, k))