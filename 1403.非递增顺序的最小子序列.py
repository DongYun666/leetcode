from typing import List
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        nums_sum = sum(nums)-nums[0]
        res = [nums[0]]
        now_sum = nums[0]
        for x in nums[1:]:
            if now_sum > nums_sum:
                return res

            res.append(x)
            now_sum+=x
            nums_sum-=x
        return res
nums = [4,4,7,6,7]
print(Solution().minSubsequence(nums))
