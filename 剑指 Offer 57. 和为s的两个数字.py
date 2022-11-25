from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first,end = 0,len(nums)-1
        while nums[end]>target:
            end-=1
        while first < end:
            if nums[first]+nums[end]<target:
                first+=1
            elif nums[first]+nums[end]>target:
                end-=1
            else:
                return [nums[first],nums[end]]



nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums,target))