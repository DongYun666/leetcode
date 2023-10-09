import heapq
from typing import List
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = 0
        target = nums_sum / 2
        while nums_sum > target:
            res += 1
            temp = -heapq.heappop(nums)
            nums_sum -= temp/2
            heapq.heappush(nums, -temp/2)
        return res    
nums = [5,19,8,1]
print(Solution().halveArray(nums))