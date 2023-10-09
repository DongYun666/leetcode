from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        res_max = cur_max = float('-inf')
        res_min = cur_min = float('inf')
        sum_ = 0
        for num in nums:
            sum_ += num
            cur_max = max(cur_max + num, num)
            res_max = max(res_max, cur_max)
            cur_min = min(cur_min + num, num)
            res_min = min(res_min, cur_min)
        return max(res_max, sum_ - res_min) if res_max > 0 else res_max
    
nums = [5,-3,5]
nums = [1,-2,3,-2]
nums = [3,-2,2,-3]
nums = [-3,-2,-3]
print(Solution().maxSubarraySumCircular(nums))
