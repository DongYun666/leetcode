# -*- codeing = utf-8 -*-
# @Time : 2021/12/6 19:34
# @Author : DongYun
# @File : 1770.执行乘法运算的最大分数.py
# @Software : PyCharm
from typing import List

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        def dfs(i,k,j):
            if j == len(multipliers):
                return 0
            left = nums[i]*multipliers[j] +dfs(i+1,k,j+1)
            right = nums[k]*multipliers[j]+dfs(i,k-1,j+1)
            return max(left,right)
        return dfs(0,len(nums)-1,0)
    def maximumScore2(self, nums: List[int], multipliers: List[int]) -> int:

        def dfs(i,k,j):
            if j == len(multipliers):
                return 0
            return max(nums[i]*multipliers[j] +dfs(i+1,k,j+1),nums[k]*multipliers[j]+dfs(i,k-1,j+1))
        return dfs(0,len(nums)-1,0)


    def maximumScore3(self, nums: List[int], multipliers: List[int]) -> int:
        dp = [[0]*len(nums)]*len(nums)
        print(dp)

        def dfs(i,k,j):
            if j == len(multipliers):
                return 0
            left = nums[i]*multipliers[j] +dfs(i+1,k,j+1)
            right = nums[k]*multipliers[j]+dfs(i,k-1,j+1)
            dp[i][j] = max(left,right)
            return max(left,right)
        dfs(0,len(nums)-1,0)

        print(dp)
        return 0

    def maximumScore3(self, nums: List[int], multipliers: List[int]) -> int:
        resoult = float("-inf")
        n = len(nums)
        m = len(multipliers)
        dp = [[0 for i in range(n+1)] for i in range(n+1)]
        for i in range(1,m+1):
            dp[i][0] = dp[i-1][0] + nums[i-1] * multipliers[i-1]
        for j in range(1,m+1):
            dp[0][j] = dp[0][j-1] + nums[n-j] * multipliers[j-1]
        print(dp)
        for i in range(1,m+1):
            for j in range(1,m-i+1):
                dp[i][j] = max(dp[i - 1][j] + nums[i-1] * multipliers[i+j-1], dp[i][j-1] + nums[n-j] * multipliers[i+j-1])
        print(dp)
        for x in dp:
            resoult = max(resoult,max(x))
        return resoult
print(Solution().maximumScore3([-854,-941,10,299,995,-346,294,-393,351,-76,210,897,-651,920,624,969,-629,985,-695,236,637,-901,-817,546,-69,192,-377,251,542,-316,-879,-764,-560,927,629,877,42,381,367,-549,602,139,-312,-281,105,690,-376,-705,-906,85,-608,639,752,770,-139,-601,341,61,969,276,176,-715,-545,471,-170,-126,596,-737,130],
                               [83,315,-442,-714,461,920,-737,-93,-818,-760,558,-584,-358,-228,-220]))