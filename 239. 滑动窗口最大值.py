import heapq
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        for i in range(k):
            heapq.heappush(window,(-nums[i],i))
        res = [-window[0][0]]
        for i in range(k,len(nums)):
            heapq.heappush(window,(-nums[i],i))
            while window[0][1] <= i-k:
                heapq.heappop(window)
            res.append(-window[0][0])
        return res
    
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution().maxSlidingWindow(nums,k))