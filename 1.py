from collections import Counter, defaultdict
from typing import List
class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        indexs = defaultdict(list)
        for i,num in enumerate(nums):
            indexs[num].append(i)
        res = float("inf")
        for index in indexs.values():
            pans = 0
            for i in range(len(index)):
                k = (index[i] - index[i-1] + len(nums) - 1) % len(nums)
                pans = max(pans,(k + 1)//2)
            res = min(res,pans)
        return res

nums = [2,1,3,3,2]

nums = [15,14,14,19]

# nums = [1,2,1,2]

# nums = [5,5,5,5]

# nums = [8,8,9,10,9]

# nums = [1,11,11,11,19,12,8,7,19]
print(Solution().minimumSeconds(nums))