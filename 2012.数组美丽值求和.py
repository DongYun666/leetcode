from typing import List
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        max_ = nums[0]
        min_ = nums[-1]
        temp = [False]
        count = 0
        for i in range(1,len(nums)):
            if max_<nums[i]:
                temp.append(True)
                max_ = nums[i]
            else:
                temp.append(False)
        for i in range(len(nums)-2,0,-1):
            if min_<nums[i]:
                min_ = nums[i]
                count+=2
            elif nums[i-1]<nums[i]<nums[i+1]:
                count+=1
        return count

nums = []
print(Solution().sumOfBeauties(nums))