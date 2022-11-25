from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []
        start,end = intervals[0][0],intervals[0][1]
        for x,y in intervals[1:]:
            if y<=end:
                continue
            if x>end:
                res.append([start,end])
                start,end = x,y
            else:
                end = max(end,y)
        res.append([start,end])
        return res



intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

intervals = [[1,4],[4,5]]
#
intervals = [[1,4],[0,4]]
#
intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
print(Solution().merge(intervals))