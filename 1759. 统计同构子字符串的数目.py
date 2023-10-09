class Solution:
    def countHomogenous(self, s: str) -> int:
        cur = s[0]
        cur_len = 0
        res = 0
        MOD = 10**9+7
        for c in s:
            if c == cur:
                cur_len += 1
            else:
                res += (cur_len*(cur_len+1)//2)%MOD
                cur = c
                cur_len = 1
        return (res+cur_len*(cur_len+1)//2) %MOD




s = "abbcccaa"
s = "yyyyyyyyvvvvvvvvvvv"
print(Solution().countHomogenous(s))