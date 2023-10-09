class Solution:
    def finalString(self, s: str) -> str:
        res = []
        for c in s:
            if c == "i":
                res = res[::-1]
            else:
                res.append(c)
        return "".join(res)

s = "string"

s = "poiinter"
print(Solution().finalString(s))