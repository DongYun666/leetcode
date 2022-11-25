from typing import List
class Solution:
    def totalSteps1(self, nums: List[int]) -> int:
        res = 0
        while sum(nums[i-1]>nums[i] for i in range(1,len(nums))):
            temp = [nums[0]]
            for i in range(1,len(nums)):
                if nums[i-1]>nums[i]:
                    continue
                else:
                    temp.append(nums[i])
            nums = temp[:]
            res+=1
        return res

    def totalSteps(self, nums: List[int]) -> int:
        temp = [0 for _ in range(len(nums))]
        cur = nums[0]
        res = 0
        for i in range(1,len(nums)):
            if nums[i]>=cur:
                cur = nums[i]
            else:
                temp[i]=temp[i-1]+1
                res = max(res,temp[i])
        return res




nums = [5,3,4,4,7,3,6,11,8,5,11]
print(Solution().totalSteps(nums))