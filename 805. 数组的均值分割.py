from collections import defaultdict
from typing import List

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        nums_sum = sum(nums)
        dict = []
        for k in range(1,int(n//2)+1):
            if k*nums_sum/n % 1 == 0:
                dict.append((k,k*nums_sum//n))
        # 从nums 中选出k个数使和为target
        # def dfs(index,k,target):
        #     if k == 0 and target == 0:
        #         return True
        #     if index == len(nums) or k<=0 or target<0: #选择完
        #         return False
        #     for i in range(index,len(nums)):
        #         return dfs(index+1,k-1,target-nums[i]) or dfs(index+1,k,target)
        dp = [0] * (nums_sum+1)
        dp[0] = 1<<0
        for num in nums:
            for i in range(nums_sum,num-1,-1):
                if dp[i-num]!=0:
                    dp[i] |= (dp[i-num]<<1)
        for k,sum_ in dict:
            if dp[sum_]&(1<<k):
                return True
        return False




nums = [1, 2, 3, 4, 5, 6, 7, 8]

nums = [3,1]
#
# nums = [3,1,2]
print(Solution().splitArraySameAverage(nums))