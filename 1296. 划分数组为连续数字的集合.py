from collections import Counter
from typing import List

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k != 0:
            return False
        nums.sort()
        cnt = Counter(nums)
        for num in nums:
            if cnt[num] == 0:
                continue
            for x in range(num,num+k):
                if cnt[x] == 0:
                    return False
                cnt[x] -= 1
        return True

nums = [3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11]
k = 3

nums = [1,2,3,4,3,3]
k = 3
print(Solution().isPossibleDivide(nums, k))