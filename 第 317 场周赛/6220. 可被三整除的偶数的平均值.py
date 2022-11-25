from typing import List

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count = 0
        sum_= 0
        for num in nums:
            if num%6 == 0:
                sum_+=num
                count+=1

        return sum_//count if count != 0 else 0



nums = [1,2,4,7,10]
print(Solution().averageValue(nums))