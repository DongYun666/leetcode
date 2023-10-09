from typing import List
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = nums[0]
        dp[1][0] = nums[0]
        for i in range(1,n):
            dp[0][i] = max(dp[0][i-1] + nums[i],nums[i])
            dp[1][i] = min(dp[1][i-1] + nums[i],nums[i])
        return max(abs(max(dp[0])),abs(min(dp[1])))
nums = [1,-3,2,3,-4]
# nums = [2,-5,1,-4,3,-2]
print(Solution().maxAbsoluteSum(nums))