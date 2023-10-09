class Solution:
    def numPermsDISequence(self, s: str) -> int:
        nums = list(range(len(s) + 1))
        n = len(nums)
        res = 0
        dp = [[[nums[0]]]] + [[] for _ in range(n - 1)]
        for i in range(1, n):
            for pmt in dp[i-1]:
                for j in range(i):
                    # 将nums[i]插入到pmt的第j个位置
                    if s[j] == "I" and nums[i] < pmt[j]:
                        res = (res + 1) % (10**9 + 7)
                    elif s[j] == "D" and nums[i] > pmt[j]:
                        res = (res + 1) % (10**9 + 7)
        return res
s = "DID"
print(Solution().numPermsDISequence(s))