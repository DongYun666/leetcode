from collections import defaultdict
from typing import List
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        dect = defaultdict(list)
        for i,num in enumerate(nums):
            dect[num].append(i)
        res = 0
        def maxLength(nums, target):
            n = len(nums)
            preSum = [0] * (n)
            for i in range(1, n):
                preSum[i] = preSum[i-1] + (nums[i] - nums[i-1] - 1)
            ans = 1
            start = 0
            for end in range(1, n):
                while preSum[end] - preSum[start] > target:
                    start += 1
                ans = max(ans, end - start + 1)
            return ans
        for key,value in dect.items():
            res = max(res,maxLength(value,k))
        return res
    
nums = [1,1,2,2,1,1]
k = 2

# nums = [4,2,7,2,1,7,2]
# k = 1
print(Solution().longestEqualSubarray(nums, k))