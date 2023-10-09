import math
from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        m = len(nums)
        gcd_matrix = [[0]*m for _ in range(m)]
        for i in range(m):
            for j in range(i+1,m):
                gcd_matrix[i][j] = math.gcd(nums[i],nums[j])
        f = [0] * (1<<m)
        for k in range(1<<m):
            if not (cnt := k.bit_count()) & 1:
                for i in range(m):
                    if k>>i & 1:
                        for j in range(i+1,m):
                            if k>>j & 1:
                                f[k] = max(f[k],f[k^(1<<i)^(1<<j)]+cnt//2*gcd_matrix[i][j])
        return f[-1]

nums = [3, 4, 6, 8]
print(Solution().maxScore(nums))