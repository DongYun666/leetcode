from typing import List
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        odd = [0 for i in range(n)]
        even = [0 for i in range(n)]
        for i in range(n):
            if i % 2 == 0:
                even[i] = even[i-1] + nums[i]
                odd[i] = odd[i-1]
            else:
                even[i] = even[i-1]
                odd[i] = odd[i-1] + nums[i]
        res = 0
        for i in range(n):
            if even[i-1] + odd[n-1] - odd[i] == odd[i-1] + even[n-1] - even[i]:
                res += 1
        return res
        

nums = [2,1,6,4]
print(Solution().waysToMakeFair(nums))