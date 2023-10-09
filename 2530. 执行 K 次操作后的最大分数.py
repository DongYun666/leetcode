from heapq import heapify, heappush
from math import ceil
from typing import List
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        res = 0
        for num in nums:
            heappush(heap,-num)
        for i in range(k):
            temp = -heap.pop(0)
            res += temp
            heappush(heap,-ceil(temp/3))
        return res
    
nums = [10,10,10,10,10]
k = 5
print(Solution().maxKelements(nums,k))