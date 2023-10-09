import heapq
from typing import List
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        res = float('-inf')
        n = len(points)
        temp = []
        for x,y in points:
            while temp and x - temp[0][1] > k:
                heapq.heappop(temp)
            if temp:
                res = max(res, x + y - temp[0][0])
            heapq.heappush(temp,(x - y,x))
        return res
points = [[1,3],[2,0],[5,10],[6,-10]]
k = 1

points = [[0,0],[3,0],[9,2]]
k = 3
print(Solution().findMaxValueOfEquation(points,k))