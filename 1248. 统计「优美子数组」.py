from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd = [-1]
        res = 0
        for i in range(len(nums)):
            if nums[i] & 1:
                odd.append(i)
        odd.append(len(nums))
        for i in range(1,len(odd)-k):
            res += (odd[i]-odd[i-1]) * (odd[i+k]-odd[i+k-1])
        return res




nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
k = 2
print(Solution().numberOfSubarrays(nums, k))