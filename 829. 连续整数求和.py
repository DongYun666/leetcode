class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        res = 0
        for i in range(0,n):
            a = n/(i + 1) - i / 2
            if a < 1:
                break
            if a == int(a):
                res += 1
        return res
print(Solution().consecutiveNumbersSum(5))