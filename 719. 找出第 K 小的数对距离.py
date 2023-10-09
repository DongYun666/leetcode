import bisect
import functools
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count(mid: int) -> int:
            cnt = 0
            for j, num in enumerate(nums):
                i = bisect.bisect(nums, num - mid, 0, j)
                cnt += j - i
            return cnt

        nums.sort()
        return bisect.bisect(range(nums[-1] - nums[0]), k, key = functools.cmp_to_key(count))


    
nums = [1,6,1]
k = 3
print(Solution().smallestDistancePair(nums,k))