class Solution:
    def findNthDigit(self, n: int) -> int:
        i = 1
        while n > i * 9 * 10 ** (i - 1):
            n -= i * 9 * 10 ** (i - 1)
            i += 1
        a, b = divmod(n - 1, i)
        return int(str(10 ** (i - 1) + a)[b])
n = 1000000000
print(Solution().findNthDigit(n))