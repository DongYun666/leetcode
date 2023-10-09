from collections import defaultdict
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res,pre = 0,0
        mp = defaultdict(int)
        mp[0] = 1
        n = len(nums)
        for i in range(n):
            pre += nums[i]
            if mp[pre-k]:
                res += mp[pre-k]
            mp[pre] += 1
        return res

    
nums = [1,1,1]
k = 2

nums = [1,2,3]
k = 3

# nums = [1]
# k = 0
print(Solution().subarraySum(nums, k))