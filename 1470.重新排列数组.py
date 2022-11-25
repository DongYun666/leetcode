from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[n-i-1])
        return res

nums = [1, 2, 3, 4, 4, 3, 2, 1]
n = 4
print(Solution().shuffle(nums,n))

