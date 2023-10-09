from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []
        n = len(nums)
        for index in range(n * 2 - 1):
            while stack and nums[stack[-1]] < nums[index % n]:
                res[stack.pop()] = nums[index % n]
            stack.append(index % n)
        return res




nums = [1,2,3,4,3]
print(Solution().nextGreaterElements(nums))