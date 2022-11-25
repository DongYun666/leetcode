import math
from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        def count(num):
            c = 0
            ans = 0
            for i in range(1,int(math.sqrt(num))+1):
                if num % i == 0:
                    if num // i == i:
                        c+=1
                        ans+=i
                    else:
                        c+=2
                        ans+=i
                        ans+=num//i
            if c != 4:
                return 0
            return ans


        for num in nums:
            res+=count(num)
        return res



nums = [21,21]
print(Solution().sumFourDivisors(nums))