class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9+7
        count = [0]*26
        res = 1
        count[ord(s[0])-ord('a')] = 1
        for c in s[1:]:
            t = count[ord(c)- ord('a')]
            count[ord(c)-ord('a')] = (res+1)%mod
            res = (res-t+res+1)%mod
        return res


s = "aaa"
s = "abc"
# s = "aba"
print(Solution().distinctSubseqII(s))
