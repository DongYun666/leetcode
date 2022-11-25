from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_,min_ = [0]*len(nums),[0]*len(nums)
        max_[0]=min_[0] = nums[0]
        res = float("-inf")
        for i in range(1,len(nums)):
            max_[i]=max(max_[i-1]*nums[i],max(nums[i],nums[i]*min_[i-1]))
            min_[i]=min(min_[i-1]*nums[i],min(nums[i],nums[i]*max_[i-1]))
            # res = max(max_[i],min_[i])
        return max(max_)

nums = [2,3, -2, 4]
# nums = [-2,0,-1]
print(Solution().maxProduct(nums))
