from typing import List
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        remain_0 = sorted([num for num in nums if num % 3 == 0],reverse=True)
        remain_1 = sorted([num for num in nums if num % 3 == 1],reverse=True)
        remain_2 = sorted([num for num in nums if num % 3 == 2],reverse=True)
        total,remove = sum(nums),float('inf')
        if total % 3 == 0:
            remove = 0
        if total % 3 == 1:
            if len(remain_1) >= 1:
                remove = min(remove,remain_1[-1])
            if len(remain_2) >= 2:
                remove = min(remove,remain_2[-2]+remain_2[-1])
        if total % 3 == 2:
            if len(remain_1) >= 2:
                remove = min(remove,remain_1[-2]+remain_1[-1])
            if len(remain_2) >= 1:
                remove = min(remove,remain_2[-1])
        return total-remove
    
nums = [3,6,5,1,8]
# nums = [1,2,3,4,4]
print(Solution().maxSumDivThree(nums))