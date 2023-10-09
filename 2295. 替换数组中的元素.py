from typing import List

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dect = {num:i  for i, num in enumerate(nums)}
        for x,y in operations:
            index = dect[x]
            nums[index] = y
            del dect[x]
            dect[y] = index
        return nums
        print(dect)

nums = [1,2,4,6]
operations = [[1,3],[4,7],[6,1]]
print(Solution().arrayChange(nums, operations))