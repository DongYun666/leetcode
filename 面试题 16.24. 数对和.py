from collections import defaultdict
from typing import List
class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        dect = defaultdict(int)
        res = []
        for num in nums:
            if dect[target-num]:
                dect[target-num] -= 1
                res.append([num,target-num])
            else:
                dect[num] += 1
        return res
nums = [5,6,5,6]
target = 11
print(Solution().pairSums(nums, target))