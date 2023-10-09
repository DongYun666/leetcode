from typing import List
class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        dect = [[] for _ in range(n)]
        for l,r,c in offers:
            dect[r].append((l,c))
        dp = [0] * n
        for i in range(n):
            if i:
                dp[i] = max(dp[i],dp[i-1])
            for l,c in dect[i]:
                dp[i] = max(dp[i],(dp[l-1] if l else 0)+c)
        return dp[-1]

  
n = 5
offers = [[0,0,1],[0,2,10],[1,3,2]]

# n = 5
# offers = [[0,0,1],[0,2,2],[1,3,2]]
print(Solution().maximizeTheProfit(n, offers))
