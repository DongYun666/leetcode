from math import gcd
from typing import List

class Solution:
    def subarrayGCD1(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i]%k:
                nums[i] = -1
            else:
                nums[i] = nums[i]//k
        res = 0
        record_1 = []
        flag = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                res+=(i-flag)+1
                if len(record_1)!=0:
                    for r in record_1:
                        if r>flag:
                            res+=i-r
                record_1.append(i)
            elif nums[i] == -1 and nums[i-1] != -1:
                flag = i-1
            else:
                continue
        return res
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            g = 0
            for j in range(i,len(nums)):
                g = gcd(g, nums[j])
                if g == k:res+=1
        return res


nums = [9, 3, 1, 2, 6, 3]
k = 3
print(Solution().subarrayGCD(nums, k))