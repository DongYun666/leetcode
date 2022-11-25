from collections import defaultdict
from typing import List

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        count = defaultdict(int)
        ans = 0
        for num in nums:
            count[num%space]+=1
            ans = max(ans,count[num%space])
        res = float(float("inf"))
        for num in nums:
            if count[num%space] == ans:
                res = min(res,num)
        return res


nums = [1,5,3,2,2]
space = 10000
nums = [1,3,5,2,4,6]
space = 2
print(Solution().destroyTargets(nums,space))