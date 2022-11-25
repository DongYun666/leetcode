from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(len(nums)-1,i,-1):
                if nums[j]>=nums[i]:
                    res = max(res,j-i)
        return res


nums = [9,8,1,0,1,9,4,0,4,1]

nums = [6,0,8,2,1,5]

print(Solution().maxWidthRamp(nums))