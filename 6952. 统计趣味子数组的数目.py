from typing import List
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        res = 0
        temp = []
        for i in range(len(nums)):
            temp.append(int(nums[i] % modulo == k))
        for i in range(len(temp)):
            cur_sum = temp[i]
            if cur_sum % modulo == k:
                res += 1
            for j in range(i+1,len(temp)):
                cur_sum += temp[j]
                if cur_sum % modulo == k:
                    res += 1
        return res

nums = [3,1,9,6]
modulo = 3
k = 0

# nums = [3,2,4]
# modulo = 2
# k = 1
print(Solution().countInterestingSubarrays(nums, modulo, k))