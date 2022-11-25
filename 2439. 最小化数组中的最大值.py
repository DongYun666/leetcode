from typing import List

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        #计算前缀和
        pre_sum = [0]*len(nums)
        pre_sum[0] = nums[0]
        for i in range(1,len(nums)):
            pre_sum[i] = pre_sum[i-1]+nums[i]
        for i in range(1,len(nums)):
            if res<nums[i]:
                temp = pre_sum[i]/(i+1)
                res = int(temp)+1 if temp%1 != 0 else int(temp)
        return res




nums = [3, 7, 1, 6]

# nums = [10,1]

nums = [13,13,20,0,8,9,9]

nums = [4,7,2,2,9,19,16,0,3,15]
print(Solution().minimizeArrayValue(nums))