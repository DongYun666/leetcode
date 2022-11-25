class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def count_hashValue(s,p,m):
            res = 0
            k = 0
            for w in s:
                res+=(ord(w)-97+1)*p**k
                k+=1
            return res%m
        for i in range(len(s)-k):
            # print(s[i:i+k])
            if hashValue == count_hashValue(s[i:i+k],power,modulo):
                return s[i:i+k]





s = "leetcode"
power = 7
modulo = 20
k = 2
hashValue = 0
print(Solution().subStrHash(s, power, modulo, k,hashValue))