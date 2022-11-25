from collections import defaultdict
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        dict = defaultdict(int)
        dict[nums[0]%k] = 0
        dict[0] = -1
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
            if nums[i]%k in dict.keys():
                if i - dict[nums[i]%k]>1:
                    return True
            else:
                dict[nums[i]%k] += i
        return False



nums = [23, 2,4,6,6]
k = 7

# nums = [2,4,3]
# k = 6
print(Solution().checkSubarraySum(nums, k))