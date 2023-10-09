from typing import List
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        temp = target // 2
        if temp > n:
            return n * (n + 1) // 2
        else:
            res = temp * (temp + 1) // 2
            res += (2 * target + n - temp - 1) * (n - temp) // 2
        return res
n = 1
target = 1
print(Solution().minimumPossibleSum(n, target))
