from math import gcd
from typing import List

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        mx = max(nums)
        occur = [False] * (mx+1)
        res = 0
        for num in nums:
            occur[num] = True
        for i in range(1,mx+1):
            g = 0
            for j in range(i,mx+1,i):
                if occur[j]:
                    g = gcd(g,j)
                    if g == i:
                        res += 1
                        break
        return res

nums = [6, 10, 3]
nums = [5,15,40,5,6]
print(Solution().countDifferentSubsequenceGCDs(nums))