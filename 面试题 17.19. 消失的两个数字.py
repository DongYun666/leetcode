from typing import List
class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        x = 0
        for i in range(len(nums)):
            x ^= nums[i]
            x ^= i
        n = len(nums)
        x = x^n^(n+1)^(n+2)
        temp = x&(-x)
        d_1_1 = 0
        for i in range(1,n+3):
            if temp & i:
                d_1_1 ^= i
        for j in nums:
            if temp & j:
                d_1_1 ^= j
        return [d_1_1,x^d_1_1]





nums = [2,3]
print(Solution().missingTwo(nums))