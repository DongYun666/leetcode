from collections import defaultdict
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        valid = True             
        visted = [0] * numCourses
        edges = defaultdict(list) 
        
        for u, v in prerequisites:
            edges[v].append(u)

        def dfs(u):               
            nonlocal valid       
            visted[u] = 1
            for v in edges[u]:
                if visted[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visted[v] == 1:
                    valid = False
                    return
            visted[u] = 2
        for i in range(numCourses):
            if valid and not visted[i]:
                dfs(i)
        return valid

numCourses = 2
prerequisites = [[1,0],[0,1]]


# numCourses = 2
# prerequisites = [[0,1]]


print(Solution().canFinish(numCourses, prerequisites))