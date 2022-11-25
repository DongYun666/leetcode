from typing import List

class Solution:
    def sumSubseqWidths1(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        mod = 10**9+7
        for i in range(len(nums)):
            t = 1
            for j in range(i+1,len(nums)):
                res = (res+(nums[j] - nums[i])*t)%mod
                t<<=1
        return res
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        mod = 10**9+7
        n = len(nums)
        for i in range(n):
            if i == 0:
                t = -2**(n-1)+1
            elif i == len(nums)-1:
                t = 2**(n-1)-1
            else:
                t = ((2<<(i-1))-(2<<(n-2-i))) % mod
            res = (res+t*nums[i]) % mod
        return res



nums = [2, 1, 3]

# nums = [2]

# nums = [2,3,3,7]
# nums = [1,2,3,4]
print(Solution().sumSubseqWidths(nums))

# print(2<<0)
# print(2<<3)