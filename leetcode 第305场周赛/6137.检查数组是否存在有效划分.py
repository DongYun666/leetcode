from typing import List
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return False
        if nums[0]==nums[1] or nums[0]==nums[1]==nums[2] or (nums[1]-nums[0]==1 and nums[2]-nums[1]==0):
            return True
        else:
             return self.validPartition(nums[2:]) or self.validPartition(nums[3:])
        return False




# nums = [4, 4, 4, 5, 6]
nums = [1,1,1,2]
print(Solution().validPartition(nums))