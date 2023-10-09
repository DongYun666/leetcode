from typing import List

# 使用二分查找
class Solution:
    def binarysearch(self, nums: List[int], target: int, flag: bool) -> int:
        n = len(nums)
        l, r = 0, n - 1
        res = n
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target or (flag and nums[mid] >= target):
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        return res  
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarysearch(nums, target, True)
        right = self.binarysearch(nums, target, False) - 1
        if left <= right and right < len(nums):  
            return [left, right]
        return [-1, -1]
        
nums = [5,7,7,8,8,10]
target = 8

# nums = [5,7,7,8,8,10]
# target = 6

nums = [1]
target = 1

print(Solution().searchRange(nums, target))