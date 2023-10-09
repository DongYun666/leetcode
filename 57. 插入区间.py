from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        res = []
        first,right = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= right:
                right = max(right,interval[1])
            else:
                res.append([first,right])
                first,right = interval
        res.append([first,right])
        return res
    
    def insert1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left,right = newInterval
        res = []
        for l,r in intervals:
            if r < left:
                res.append([l,r])
            elif l > right:
                res.append([left,right])
                left,right = l,r
            else:
                left = min(left,l)
                right = max(right,r)
        res.append([left,right])
        return res
    
intervals = [[1,3],[6,9]]
newInterval = [2,5]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]  
newInterval = [4,8]
print(Solution().insert1(intervals, newInterval))


