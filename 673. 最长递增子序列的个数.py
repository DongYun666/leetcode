from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        import bisect
        dp = [1]
        for num in nums[1:]:
            i = bisect.bisect_left(dp, num)
            if i == len(dp) and num > nums[i-1]:
                dp.append(i+1)
            else:
                dp.append(dp[i-1])
        return dp.count(max(dp))
    
nums = [1,3,5,4,7]
print(Solution().findNumberOfLIS(nums)) # 2