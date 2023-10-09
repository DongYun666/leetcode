from typing import List
class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        nums.sort()
        n = len(nums)
        preSum = 0
        currsum = 0
        res = 0
        for i in range(n):
            currsum = preSum + nums[i]
            preSum = preSum + currsum 
            res = (res + nums[i]**2 * currsum )  % mod
        return res % mod

nums = [1,2,3,4]
nums = [2,1,4]
print(Solution().sumOfPower(nums))