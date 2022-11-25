from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s_1 = Counter(s1)
        for i in range(len(s2)-len(s1)+1):
            temp = Counter(s2[i:i+len(s1)])
            if temp == s_1:
                return True
        return False



s1 = "ab"
s2 = "eidbaooo"

s1= "ab"
s2 = "eidboaoo"

s1 = "adc"
s2 = "dcda"
print(Solution().checkInclusion(s1, s2))