from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        temp = []
        for time in timePoints:
            t = time.split(":")
            temp.append([int(t[0]), int(t[1])])
        temp.sort(key = lambda x:x[0])
        print(temp)
        res = (temp[1][0]-temp[0][0])*60+(temp[1][1]-temp[0][1])
        return min(res,1440-res)



timePoints = ["01:01","02:01","03:00"]
print(Solution().findMinDifference(timePoints))