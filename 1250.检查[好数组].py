from typing import List
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def GCD(a,b):
            if b == 0:
                return a;
            else:
                return GCD(b,a%b)
        def GCDN(digets,lenght):
            if lenght == 1:
                return digets[0]
            else:
                return GCD(digets[lenght-1],GCDN(digets,lenght-1))
        return True if GCDN(nums,len(nums)) == 1 else False





nums = [12,5,7,23]
print(Solution().isGoodArray(nums))