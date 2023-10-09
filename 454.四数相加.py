from collections import Counter
from typing import List
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res = 0
        union12 = Counter([x+y for x in nums1 for y in nums2])
        for x in nums3:
            for y in nums4:
                if -x-y in union12:
                    res += union12[-x-y]
        return res
nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
print(Solution.fourSumCount(Solution,nums1,nums2,nums3,nums4))