from collections import defaultdict
class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        temp = ["" for _ in range(len(s))]
        for i in range(len(s)):
            temp[int(s[i][-1])-1] = s[i][:-1]
        return " ".join(temp)


s = "is2 sentence4 This1 a3"
print(Solution().sortSentence(s))