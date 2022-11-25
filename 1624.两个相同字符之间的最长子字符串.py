from collections import defaultdict


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = defaultdict()
        ans = -1
        for index,w in enumerate(s):
            if w not in first:
                first[w] = index
            else:
                ans = max(ans,index-first[w]-1)
        return ans



s = "aa"
print(Solution().maxLengthBetweenEqualCharacters(s))