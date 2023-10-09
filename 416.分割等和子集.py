from typing import List

class Solution:
    def canPartition1(self, nums: List[int]) -> bool:
        sub_sum = sum(nums)
        if sub_sum % 2 != 0:
            return False
        sub_sum //= 2
        def dfs(index,cur_sum):
            if cur_sum > sub_sum or index == len(nums):
                return False
            if cur_sum == sub_sum:
                return True
            return dfs(index+1,cur_sum+nums[index]) or dfs(index+1,cur_sum)
        return dfs(0,0)
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target & 1:return False
        target //= 2
        n = len(nums)
        dp = [[False]*(target+1) for _ in range(n)]
        for i in range(n): dp[i][0] = True
        dp[0][nums[0]] = True
        for i in range(1,n):
            num = nums[i]
            for j in range(1,target+1):
                if j == num:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-num]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n-1][target]
    
    def canPartition2(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:return False
        target = total // 2
        n = len(nums)
        dp = [True] + [False] * (target)
        for i in range(n):
            for j in range(target,nums[i]-1,-1):
                dp[j] |= dp[j-nums[i]]
        return dp[target]

nums = [1,5,11,5]
print(Solution().canPartition2(nums))