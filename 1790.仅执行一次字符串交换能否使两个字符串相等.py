class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        i,j = -1,-1
        for index,w in enumerate(s1):
            if s1[index] != s2[index]:
                if i<0:
                    i = index
                elif j < 0:
                    j = index
                else:
                    return False
        return (i<0 and j<0) or (i>=0 and j>=0 and s1[i] == s2[j] and s1[j] == s2[i])


s1 = "bank"
s2 = "kanb"

s1 = "attack"
s2 = "defend"
print(Solution().areAlmostEqual(s1, s2))