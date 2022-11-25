from collections import Counter


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return Counter(s1) == Counter(s2)

num = []
num.insert(0,6)

print(num)



# s1 = "abc"
# s2 = "bad"
# print(Solution().CheckPermutation(s1, s2))


