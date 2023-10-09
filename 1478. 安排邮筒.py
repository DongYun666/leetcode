from typing import List
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        dp = [[0]*n for _ in range(k)]
        for i in range(n):
            dp[0][i] = sum([abs(houses[i]-houses[j]) for j in range(i+1)])
        for i in range(1,k):
            for j in range(i,n):
                dp[i][j] = min([dp[i-1][j]+sum([abs(houses[j]-houses[t]) for t in range(j)])])
        return dp[-1][-1]
    
houses = [1,4,8,10,20]
k = 3
print(Solution().minDistance(houses,k))