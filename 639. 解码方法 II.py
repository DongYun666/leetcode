class Solution:
    def numDecodings(self, s: str) -> int:
        def check(ch):
            if ch == "0":
                return 0
            return 9 if ch == "*" else 1
        def check2(ch1, ch2):
            if ch1 == ch2 == "*":
                return 15
            if ch1 == "*":
                return 2 if ch2 <= "6" else 1
            if ch2 == "*":
                if ch1 == "1":
                    return 9
                if ch1 == "2":
                    return 6
                return 0
            return int(ch1 != "0" and int(ch1) * 10 + int(ch2) <= 26)
        mod = 10**9 + 7
        n = len(s)
        dp = [0] * n
        dp[0] = check(s[0])
        if n >= 2:
            dp[1] = dp[0] * check(s[1]) + check2(s[0],s[1])
        for i in range(2,n):
            dp[i] = (dp[i-1] * check(s[i]) + (dp[i-2] if i >= 2 else 1) * check2(s[i-1],s[i])) % mod
        return dp[-1]
s = "1*"

s = "*"
print(Solution().numDecodings(s))