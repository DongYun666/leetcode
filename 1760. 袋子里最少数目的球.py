from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l,r,res = 1,max(nums),0
        while l <= r:
            mid = (l+r)//2
            y_opt = sum((num-1)//mid for num in nums)
            if y_opt<=maxOperations:
                res = mid
                r = mid-1
            else:
                l = mid +1
        return res



nums = [2, 4, 8, 2]
maxOperations = 4

# nums = [9]
# maxOperations = 2
print(Solution().minimumSize(nums, maxOperations))