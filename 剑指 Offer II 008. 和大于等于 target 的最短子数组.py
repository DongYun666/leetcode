import bisect
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        n = len(nums)
        res = n+1
        pre_sum = [0]
        for i in range(n):
            pre_sum.append(pre_sum[-1]+nums[i])
        for i in range(1,n+1):
            temp = target+pre_sum[i-1]
            end = bisect.bisect_left(pre_sum, temp)
            # print(end)
            if end != len(pre_sum):
                res = min(res,end-i+1)
        return res if res != n+1 else 0

target = 7
nums = [2, 3, 1, 2, 4, 3]

target = 4
nums = [1,4,4]

target = 11
nums = [1,1,1,1,1,1,1,1]

# target = 15
# nums = [1,2,3,4,5]

target = 7
nums = [2,3,1,2,4,3]

print(Solution().minSubArrayLen(target, nums))