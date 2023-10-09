from typing import List
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        pre = nums[0]
        res = 1
        for i in range(1, len(nums)):
            if nums[i] - pre > k:
                res += 1
                pre = nums[i]
        return res
nums = [1,2,3]
k = 1

nums = [3,6,1,2,5]
k = 2

nums = [2,2,4,5]
k = 0
print(Solution().partitionArray(nums, k))