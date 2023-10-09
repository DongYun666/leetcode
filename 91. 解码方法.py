from typing import List
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]
    

        # dp = [0 for _ in range(len(s) + 1)]
        # dp[0] = dp[1] = 1
        # pre_num = int(s[0])
        # if pre_num == 0:return 0
        # for i in range(1,len(s)):
        #     if s[i] == '0':
        #         if pre_num == 1 or pre_num == 2:
        #             dp[i+1] = dp[i]
        #         else:
        #             return 0
        #     elif pre_num == 1 or (pre_num == 2 and int(s[i]) <= 6):
        #         dp[i + 1] = dp[i] + dp[i-1]
        #     else:
        #         dp[i+1] = dp[i]
        #     pre_num = int(s[i])
        # return dp[-1]
    
s = "2226"
s = "226"
s = "06"
s = "12"
s = '102'
s = "2101"
print(Solution().numDecodings(s))