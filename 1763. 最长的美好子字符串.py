class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        res = ''
        n = len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                tmp = s[i:j]
                if all(ch.swapcase() in tmp for ch in tmp):
                    if len(tmp) > len(res):
                        res = tmp
        return res
s = "YazaAay"
# s = "Bb"
# s = "c"
print(Solution().longestNiceSubstring(s))