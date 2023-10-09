from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[1]*(n+1) for _ in range(m+1)]

        def count(str):
            one = 0
            n = len(str)
            for s in strs:
                if s == "1":
                    one += 1
            return one,n-one

        for str in strs:
            ones,zeros = count(str)
            for i in range(m,zeros-1,-1):
                for j in range(n,ones-1,-1):
                    dp[i][j] = max(dp[i][j],dp[i-zeros][j-ones]+1)
        return dp[m][n]

strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3

strs = ["10", "0", "1"]
m = 1
n = 1
print(Solution().findMaxForm(strs, m, n))