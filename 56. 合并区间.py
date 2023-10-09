from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        res = []
        for start,end in intervals:
            if not res or res[-1][1] < start:
                res.append([start,end])
            else:
                res[-1][1] = max(end,res[-1][1])
        return res

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals = [[1,4],[4,5]]
print(Solution().merge(intervals))