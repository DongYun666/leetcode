class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        # 先将两个字符串合并，然后求最长回文子序列
        word = word1 + word2
        # 求最长回文子序列
        n = len(word)
        n1 = len(word1)
        res = 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1, -1, -1):
            for j in range(i+1,n):
                if word[i] == word[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                    if i < n1 and j >= n1:
                        res = max(res,dp[i][j])
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return res

word1 = "cacb"
word2 = "cbba"

# word1 = "aa"
# word2 = "bb"
print(Solution().longestPalindrome(word1,word2))