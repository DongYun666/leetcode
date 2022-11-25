import bisect
from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        res = []
        for num in nums:
            res.append(bisect.bisect_left(temp,num))
        return res


nums = [8,1,2,2,3]
print(Solution().smallerNumbersThanCurrent(nums))