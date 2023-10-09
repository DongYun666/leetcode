from typing import List

class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        height,weight  = zip(*sorted(zip(height, weight), key=lambda x: x[0]))
        n = len(height)
        dp = [1] * n
        res = 0
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if weight[j]<weight[i]:
                    dp[i] = max(dp[i],dp[j]+1)
            res = max(res,dp[i])
        return res



height = [65, 70, 56, 75, 60, 68]
weight = [100, 150, 90, 190, 95, 110]
print(Solution().bestSeqAtIndex(height, weight))