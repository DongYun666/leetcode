from collections import defaultdict
from typing import List
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        
        res = 0
        count = defaultdict(int)
        n = len(nums)
        if n <k:
            return 0
        cur_sum = 0
        for i in range(k):
            count[nums[i]] += 1
            cur_sum += nums[i]
        if len(count.keys()) >= m:
            res = max(res,cur_sum)
        for i in range(k,n):
            count[nums[i-k]] -= 1
            if count[nums[i-k]] == 0:
                del count[nums[i-k]]
            count[nums[i]] += 1
            cur_sum += nums[i] - nums[i-k]
            if len(count.keys()) >= m:
                res = max(res,cur_sum)
        return res
    
nums = [2,6,7,3,1,7]
m = 3
k = 4

nums = [5,9,9,2,4,5,4]
m = 1
k = 3

nums = [1,2,1,2,1,2,1]
m = 3
k = 3
print(Solution().maxSum(nums, m, k))