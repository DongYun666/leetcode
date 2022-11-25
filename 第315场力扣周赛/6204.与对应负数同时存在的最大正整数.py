from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        if nums[-1]<0:
            return -1
        while nums[i]<0 and i<len(nums):
            if -nums[i] in nums:
                return -nums[i]
            i+=1
        return -1
nums = [-1, 10, 6, 7, -7, 1]
nums = [-1,2,-3,3]
print(Solution().findMaxK(nums))