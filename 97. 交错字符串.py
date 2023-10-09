class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        m,n = len(s1),len(s2)
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1,m + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1,n + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1,m + 1):
            for j in range(1,n + 1):
                p = i + j - 1
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[p]) or (dp[i][j-1] and s2[j-1] == s3[p])
        return dp[-1][-1]    

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbbaccc"
print(Solution().isInterleave(s1,s2,s3))