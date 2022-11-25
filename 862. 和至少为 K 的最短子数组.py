from collections import deque
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        presum = [0]
        for num in nums:
            presum.append(presum[-1]+num)
        print(presum)
        q = deque()
        res = len(nums)+1
        for i,ps in enumerate(presum):
            while q and ps-presum[q[0]]>=k:
                res = min(res,i-q.popleft())
            while q and presum[q[-1]] >= ps:
                q.pop()
            q.append(i)
        return res if res < len(nums)+1 else -1


nums = [2, -1, 3]
k = 3

nums = [1,2]
k = 4
print(Solution().shortestSubarray(nums, k))