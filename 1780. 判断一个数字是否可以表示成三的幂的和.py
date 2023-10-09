import math


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        x = 3 ** int(math.log(n,3))
        while n:
            if n >= x:
                n -= x
            x //= 3
            if x == 0:
                break
        return n == 0
n = 12

n = 91

n = 21
print(Solution().checkPowersOfThree(n))