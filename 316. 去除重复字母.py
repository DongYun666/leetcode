from collections import defaultdict


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res = []
        last = defaultdict(int)
        for i, c in enumerate(s):
            last[c] = i
        for i, c in enumerate(s):
            if c not in res:
                while res and res[-1] > c and i < last[res[-1]]:
                    res.pop()
                res.append(c)
        return ''.join(res)
    
s = "cbacdcbc"
print(Solution().removeDuplicateLetters(s))