from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        bit = 0
        while (n - 1) >> bit:
            bit += 1
        for i in range(bit):
            x,y = 0,0
            for index,num in enumerate(nums):
                if num & (1 << i):
                    x += 1
                if index & (1 << i):
                    y += 1
            if x > y:
                res |= 1<<i
        return res 
    
nums = [2,2,2,2,2]
print(Solution().findDuplicate(nums))