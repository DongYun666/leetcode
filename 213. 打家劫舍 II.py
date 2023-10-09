from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        return max(my_rob(nums[:-1]),my_rob(nums[1:])) if len(nums) != 1 else nums[0]
    
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:return nums[0]
        if n == 2:return max(nums)
        dp = [0 for _ in range(n)]
        dp[0],dp[1] = nums[0],max(nums[0],nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        if dp[-1] == dp[-2] and dp[0]+nums[2] == dp[2]:
            return max(dp[-1]-nums[0],dp[-2])
        else:
            return dp[-1]

nums = [1,2,3,1]
nums = [2,7,9,3,1]
print(Solution().rob(nums))
        
        
