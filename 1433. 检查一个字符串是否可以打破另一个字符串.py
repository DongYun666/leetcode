class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        s1.sort()
        s2.sort()
        return all(x>=y for x,y in zip(s1,s2)) or all(x>=y for x,y in zip(s2,s1))





s1 = "leetcodee"
s2 = "interview"
# s1 = "abe"
# s2 = "acd"
print(Solution().checkIfCanBreak(s1, s2))