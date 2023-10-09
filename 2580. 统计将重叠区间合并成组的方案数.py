from typing import List
class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort(key=lambda x: x[0])
        m,max_r = 1,ranges[0][1]
        for l,r in ranges:
            m += l > max_r
            max_r = max(max_r,r)
        return pow(2,m,10**9+7)
    
ranges = [[1,3],[10,20],[2,5],[4,8]]
print(Solution().countWays(ranges))