import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        diff = lambda x,y:(x+1)/(y+1)-x/y
        res = 0.
        temp = []
        for p,t in classes:
            res+=p/t
            temp.append([-diff(p,t),p,t])
        heapq.heapify(temp)
        for _ in range(extraStudents):
            d,p,t = heapq.heappop(temp)
            res+=-d
            heapq.heappush(temp,[-diff(p+1,t+1),p+1,t+1])
        return res/len(temp)






classes = [[1, 2], [3, 5], [2, 2]]
extraStudents = 2
print(Solution().maxAverageRatio(classes, extraStudents))