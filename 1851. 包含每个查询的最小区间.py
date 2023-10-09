from typing import List
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [-1] * len(queries)
        intervals.sort(key=lambda x: x[1] - x[0])
        for i, q in enumerate(queries):
            for interval in intervals:
                if interval[0] <= q <= interval[1]:
                    res[i] = interval[1] - interval[0] + 1
                    break
        return res
    

intervals = [[1,4],[2,4],[3,6],[4,4]]
queries = [2,3,4,5]
print(Solution().minInterval(intervals, queries))