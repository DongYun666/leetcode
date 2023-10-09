import bisect
from typing import List 
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        n = len(nums)
        res = float('inf')
        set_nums =  nums[x:]
        for i in range(n-x):
            index = bisect.bisect_left(list(set_nums),nums[i])
            if index < len(set_nums):
                res = min(res,abs(nums[i] - list(set_nums)[index]))
            if index > 0:
                res = min(res,abs(nums[i] - list(set_nums)[index-1]))
            set_nums.remove(nums[i+x])
        return res
    
# nums = [4,3,2,4]
# x = 2

# nums = [5,3,2,10,15]
# x = 1

nums = [1,2,3,4]
x = 3

nums = [83,14,14]
x = 1
print(Solution().minAbsoluteDifference(nums,x))