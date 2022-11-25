from typing import List

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        res = 0
        def lcm(x,y):
            a,b = x,y
            while y:
                x,y = y,x%y
            return a*b//x

        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i,len(nums)):
                temp = lcm(temp,nums[j])
                if temp == k:
                    res+=1

        return res



nums = [3, 6, 2, 7, 1]
k = 6

nums = [3]
k = 2
print(Solution().subarrayLCM(nums, k))