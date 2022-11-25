from typing import List

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums = list(set(nums))
        n = len(nums)
        def reverse(x):
            res = 0
            while x!=0:
                res = res*10+x%10
                x //=10
            return res
        for i in range(n):
            nums.append(reverse(nums[i]))
        nums = list(set(nums))
        return len(nums)
nums = [1,13,10,12,31]
nums = [2,2,2]
print(Solution().countDistinctIntegers(nums))