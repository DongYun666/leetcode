class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        dp = [1] * (len(num) + 1)
        for i in range(1, len(num)):
            if num[i - 1] == '0' or num[i - 1:i + 1] > '25':
                dp[i + 1] = dp[i]
            else:
                dp[i + 1] = dp[i] + dp[i - 1]
        return dp[-1]
num = 12258
print(Solution().translateNum(num))