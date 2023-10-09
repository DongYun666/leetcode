from typing import List
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        index = range(n)
        index = sorted(index,key=lambda x:nums[x])
        min_index = n
        for i in index:
            res = max(res,i-min_index)
            min_index = min(min_index,i)
        return res
nums = [6,0,8,2,1,5]
# nums = [9,8,1,0,1,9,4,0,4,1]
print(Solution().maxWidthRamp(nums))