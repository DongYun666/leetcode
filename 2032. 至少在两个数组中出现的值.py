from collections import defaultdict
from typing import List

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        dect = defaultdict(int)
        for i,nums in enumerate((nums1,nums2,nums3)):
            for num in nums:
                dect[num] |= 1<<i
        return [num for num,count in dect.items() if count&(count-1)]

nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
print(Solution().twoOutOfThree(nums1,nums2,nums3))