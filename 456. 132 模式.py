import bisect
from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        left_min = nums[0]
        right_all = sorted(nums[2:])
        for j in range(1,n-1):
            if left_min < nums[j]:
                index = bisect.bisect_right(right_all,left_min)
                if index < len(right_all) and right_all[index] < nums[j]:
                    return True
            left_min = min(left_min,nums[j])
            right_all.remove(nums[j+1])
        return False


nums = [3, 1, 4, 2]
# nums = [3,5,0,3,4]
print(Solution().find132pattern(nums))