from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        res = float("inf")
        def timetonum(t):
            t = t.split(":")
            return int(t[0])*60 + int(t[1])
        for index,time in enumerate(timePoints[1:]):
            temp = timetonum(time) - timetonum(timePoints[index-1])
            res = min(res,temp)
        return res
timePoints = ["23:59","00:00"]
print(Solution().findMinDifference(timePoints))
