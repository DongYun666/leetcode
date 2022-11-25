class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        print(dp)
        for i in range(n):
            dp[0][i] = 1
        for j in range(m):
            dp[j][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] += dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

m = 3
n = 7
print(Solution().uniquePaths(m, n))