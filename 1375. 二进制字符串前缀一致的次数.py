from typing import List
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        res = 0
        cur_sum = 0
        for i,flip in enumerate(flips):
            cur_sum += flip
            if cur_sum == (i+1)*(i+2)/2:
                res += 1
        return res
    
flips = [3,2,4,1,5]
print(Solution().numTimesAllBlue(flips))
