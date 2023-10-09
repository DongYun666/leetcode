class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        def helper(a,b):
            res = float('inf')
            for i in range(26):
                tmp = 0
                for ch in a:
                    if ord(ch) - ord('a') <= i:
                        tmp += 1
                for ch in b:
                    if ord(ch) - ord('a') > i:
                        tmp += 1
                diff = sum(1 for j in range(min(len(a),len(b))) if a[j] != b[j]) + abs(len(a) - len(b))
                res = min(res,min(diff,tmp))
            return res
        return 0 if a == b else min(helper(a,b),helper(b,a)) 
a = "acccc"
b = "bcccc"

a = "aba"
b = "caa"
print(Solution().minCharacters(a,b))