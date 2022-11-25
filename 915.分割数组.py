from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        res,left_max,cur_max = 0,nums[0],nums[0]
        for i in range(1,len(nums)):
            cur_max = max(cur_max,nums[i])
            if nums[i] < left_max:
                left_max = cur_max
                res = i
        return res+1





nums = [5,0,3,8,6]
print(Solution().partitionDisjoint(nums))