from typing import List

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        ans = 0
        temp = nums[0]
        i = 1
        cnt = 0
        while i < len(nums):
            if nums[i]<temp:
                cnt+=1
            else:
                temp = nums[i]
                ans = max(ans,cnt)
                cnt = 0
            i+=1
        return ans

nums = [5,3,4,4,7,3,6,11,8,5,11]

nums = [4,5,7,7,13]
print(Solution().totalSteps(nums))