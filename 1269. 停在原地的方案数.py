class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        t = min(steps//2+1,arrLen)
        dp = [[0 for i in range(t)]for j in range(steps+1)]
        dp[1][0] = 1
        dp[1][1] = 1
        mod = 10*9+7
        for i in range(2,steps+1):
            for j in range(t):
                dp[i][j] = dp[i-1][j]
                if j-1 >= 0:
                    dp[i][j] += dp[i-1][j-1]
                if j+1 < t:
                    dp[i][j] += dp[i-1][j+1]
                dp[i][j] %= mod
        return dp[steps][0]



steps = 4
arrLen = 3
print(Solution().numWays(steps, arrLen))