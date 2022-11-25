class Solution:
    def baseNeg2(self, n: int) -> str:
        list = []
        while n!=0:
            list.append(n%2)
            # n = -(n>>1)
            n = n//(-2)
        print(list)



n = 2
print(Solution().baseNeg2(n))