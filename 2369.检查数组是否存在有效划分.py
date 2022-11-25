from typing import List

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        f = [True]+[False]*len(nums)
        for i in range(len(nums)):
            if i > 0 and f[i-1] and nums[i] == nums[i-1] or i > 1 and f[i-2] and (nums[i] == nums[i-1] == nums[i-2] or nums[i] == nums[i-1]+1 == nums[i-2]+2):
                f[i+1] = True
        return f[len(nums)]

nums = [1,2,3,4,5,6,7]
print(Solution().validPartition(nums))