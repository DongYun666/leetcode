from functools import lru_cache
from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                left = j + 1
                right = n - 1
                target = nums[i] + nums[j]
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                res += left - j - 1
        return res
    
nums = [2,2,3,4]

nums = [4,2,3,4]
print(Solution().triangleNumber(nums))