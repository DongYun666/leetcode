from collections import defaultdict
from typing import List

class Solution:
    def longestConsecutive2(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        count = defaultdict(int)
        for num in nums:
            if num >= 0:
                if count.get(num-1, 0) == 0:
                    count[num]  = 1
                else:
                    count[num] = count[num-1] + 1
            else:
                if count.get(num+1, 0) == 0:
                    count[num]  = 1
                else:
                    count[num] = count[num+1] + 1
            res = max(res, count[num])
        print(count)
        return res
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if num-1 not in nums:
                cur = num
                temp = 1
                while cur+1 in nums:
                    cur+=1
                    temp+=1
                res = max(res,temp)
        return res

        return res

nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# nums = [100,4,200,1,3,2]
nums = [0,-1,-2]
print(Solution().longestConsecutive(nums))
