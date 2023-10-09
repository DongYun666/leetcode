from typing import List
class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        maxPair = max(a + b for a, b in zip(nums, nums[1:]))

        return maxPair >= m

nums = [2, 2, 1]
m = 4
print(Solution().canSplitArray(nums,m))


