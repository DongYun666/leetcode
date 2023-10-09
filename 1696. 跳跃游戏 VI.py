from collections import deque
from typing import List
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0]* len(nums)
        dp[0] = nums[0]
        q = [[nums[0],0]]
        for i in range(1,len(nums)):
            while q and q[0][1] < i-k:
                q.pop(0)
            dp[i] = q[0][0] + nums[i]
            while q and q[-1][0] <= dp[i]:
                q.pop()
            q.append([dp[i],i])
        return dp[-1]
    
nums = [1,-1,-2,4,-7,3]
k = 2

nums = [10,-5,-2,4,0,3]
k = 3
print(Solution().maxResult(nums,k))