from collections import Counter, defaultdict

#
# class Solution:
#     def customSortString(self, order: str, s: str) -> str:
#         v = defaultdict(int)
#         for i,c in enumerate(order):
#             v[c] = i+1
#         print(v)
#         t = sorted(s,key=lambda c:v[c])
#         return t,s
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        val = defaultdict(int)
        for i, ch in enumerate(order):
            val[ch] = i
        return "".join(sorted(s, key=lambda ch: val[ch] if ch in val else float("inf")))

order = "cba"
s = "abcd"

order = "cbafg"
s = "abcd"
print(Solution().customSortString(order, s))