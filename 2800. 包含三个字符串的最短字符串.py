from itertools import permutations


class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def merge(a,b):
            if b in a:return a
            for i in range(min(len(a),len(b)),0,-1):
                if a[-i:] == b[:i]:
                    return a + b[i:]
            return a + b
        res = a + b + c
        for a,b,c in permutations((a,b,c)):
            temp = merge(merge(a,b),c)
            if len(temp) < len(res):
                res = temp
            elif len(temp) == len(res):
                res = min(res,temp)
        return res
        # print(words)

a = "aba"
b = "ab"
c = "aaa"

# a = "cdaa"
# b = "aaef"
# c = "daaae"
print(Solution().minimumString(a,b,c))  