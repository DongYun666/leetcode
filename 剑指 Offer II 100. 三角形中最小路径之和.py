from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0]*len(triangle[-1])
        dp[0] = triangle[0][0]
        for i in range(1,len(triangle)):
            for j in range(i,-1,-1):
                if j == 0:
                    dp[j] += triangle[i][j]
                elif j == i:
                    dp[j] = dp[j-1]+triangle[i][j]
                else:
                    dp[j] = min(dp[j], dp[j-1])+triangle[i][j]
        return min(dp)


triangle = [[2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3]]
print(Solution().minimumTotal(triangle))