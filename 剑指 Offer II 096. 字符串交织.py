from collections import Counter

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        dp = [[False for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        dp[0][0] = True
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i>0:
                    dp[i][j] = dp[i][j] or (dp[i-1][j] and s1[i-1] == s3[i+j-1])
                if j>0:
                    dp[i][j] = dp[i][j] or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1][-1]
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbbaccc"

# s1 = "a"
# s2 = ""
# s3 = "a"
print(Solution().isInterleave(s1, s2, s3))