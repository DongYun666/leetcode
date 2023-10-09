from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        values = list(Counter(s).values())
        res = 0
        values.sort(reverse=True)
        n = len(values)
        for index in range(1,n):
            while values[index] >= values[index-1] and values[index] != 0:
                values[index] -= 1
                res += 1
        return res

s = "ceabaacb"
# s = "abcabc"
# s = "bbcebab"
print(Solution().minDeletions(s))