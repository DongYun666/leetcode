from collections import Counter, defaultdict
from itertools import accumulate
from typing import List
class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n,persum = len(nums),list(accumulate(nums))
        left,right,total = defaultdict(int),Counter(persum[:n-1]),persum[-1]
        print(right,total)

nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14]
k = -33
print(Solution().waysToPartition(nums, k))
