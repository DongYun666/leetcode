class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n!=0:
            if n%2==1:
                res+=1
            n>>=1
        return res
    def hammingWeight2(self, n: int) -> int:
        res = 0
        while n!=0:
            n&=n-1
            res+=1
        return res



n = 11
print(Solution().hammingWeight2(n))