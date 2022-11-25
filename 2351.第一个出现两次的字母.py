from collections import defaultdict

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = defaultdict()
        for x in s:
            d[x] = d.get(x,0)+1
            if d[x] == 2:
                return x



s = "abccbaacz"
print(Solution().repeatedCharacter(s))