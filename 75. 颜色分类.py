from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums[i],nums[left] = nums[left],nums[i]
                left += 1
        for i in range(left,n):
            if nums[i] == 1:
                nums[i],nums[left] = nums[left],nums[i]
                left += 1
nums = [2,0,2,1,1,0]
print(Solution().sortColors(nums))