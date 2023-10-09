import heapq
from typing import List
class Solution:
    def processTasks(self, tasks: List[List[int]]) -> int:
        tasks.append([10**9+1,10**9+1,1])
        res,q = 0,[]
        for start,end,d in sorted(tasks,key = lambda x:x[0]):
            while q and q[0][0] + res < start:
                if q[0][0] + res >= q[0][1]:heapq.heappop(q)
                else:res += min(q[0][1],start) - (q[0][0] + res)
            heapq.heappush(q,[end-d+1-res,end + 1])
        return res
    
tasks = [[1,3,2],[2,5,3],[5,6,2]]
# tasks = [[2,3,1],[5,5,1],[5,6,2]]
# tasks = [[0,0,1],[1,1,1],[0,10,4],[8,8,1]]
print(Solution().processTasks(tasks))