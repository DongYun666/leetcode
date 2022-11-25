from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res = 0
        l = r = -1
        for i,num in enumerate(nums):
            if left<=num<=right:
                r = i
            elif num>right:
                l = i
                r = -1
            if r != -1:
                res += r - l
        return res



nums = [2, 9, 2, 5, 6]
left = 2
right = 8

# nums = [2,1,4,3]
# left = 2
# right = 3
print(Solution().numSubarrayBoundedMax(nums, left, right))