from typing import List
class Solution:
    def checkMaxequal(self,num1,num2) -> bool:
        max_num1 = 0
        max_num2 = 0
        while num1:
            max_num1 = max(max_num1,num1 % 10)
            num1 //= 10
        while num2:
            max_num2 = max(max_num2,num2 % 10)
            num2 //= 10
        return max_num1 == max_num2
    def maxSum(self, nums: List[int]) -> int:
        res = -1
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if self.checkMaxequal(nums[i],nums[j]):
                    res = max(res,nums[i] + nums[j])
        return res
    
nums = [51,71,17,24,42]
# nums = [1,2,3,4]
print(Solution().maxSum(nums))