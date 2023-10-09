from collections import Counter
import heapq
from typing import List
class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total < target:
            return -1
        cnt = Counter(nums)
        res = 0
        for i in range(31):
            if target & (1 << i):
                cnt[1 << i] -= 1
            temp = cnt[1 << i] // 2
            if temp < 0:
                res -= temp
            cnt[1 << (i + 1)] += temp
        return res
nums = [1,32,1,2]
target = 12
print(Solution().minOperations(nums, target))