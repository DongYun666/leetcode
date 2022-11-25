class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        res = ""
        for i in range(length):
            if S[i] == ' ':
                res+="%20"
            else:
                res+=S[i]
        return res


S = "               "
length = 5
print(Solution().replaceSpaces(S, length))