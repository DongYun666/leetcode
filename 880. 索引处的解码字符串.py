class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        cur_s = ""
        cur_len = 0
        for c in s:
            if c.islower():
                cur_s += c
                cur_len += 1
                k -= 1
            else:
                target = cur_len*int(c)





S = "leet2code3"
K = 10
print(Solution().decodeAtIndex(S, K))