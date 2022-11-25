from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(1,len(nums)+1):
            if nums[i-1]>=i and (i == len(nums) or i >nums[i]):
                return i
        return -1



nums = [3,6,7,7,0]
print(Solution().specialArray(nums))