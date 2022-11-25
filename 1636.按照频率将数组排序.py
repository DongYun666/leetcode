from collections import Counter
from typing import List
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums = Counter(nums)
        nums = sorted(nums.items(),key = lambda x:(x[1],-x[0]))
        res = []
        for num,count in nums:
            res+=[num for _ in range(count)]
        return res
nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
print(Solution().frequencySort(nums))