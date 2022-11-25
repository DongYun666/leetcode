from typing import List

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        return all(abs(x-i)<=1 for i,x in enumerate(nums))




nums = [1, 3, 2]
print(Solution().isIdealPermutation(nums))