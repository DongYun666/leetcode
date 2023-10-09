from collections import Counter, defaultdict
from typing import List
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = Counter()
        res = left = pairs = 0
        for num in nums:
            pairs += count[num]
            count[num] += 1
            while pairs - count[nums[left]] + 1 >= k:
                count[nums[left]] -= 1
                pairs -= count[nums[left]]
                left += 1
            if pairs >= k:
                res += left + 1
        return res
nums = [1,1,1,1,1]
k = 10
print(Solution().countGood(nums,k))