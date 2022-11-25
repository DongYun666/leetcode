from typing import List

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        now = 0
        res = 0
        for rung in rungs:
            res+=(rung-now-1)//dist
            now = rung
        return res



rungs = [1, 3, 5, 10]
dist = 2

# rungs = [3,6,8,10]
# dist = 3
#
# rungs = [3,4,6,7]
# dist = 2
# #
# rungs = [5]
# dist = 10
print(Solution().addRungs(rungs, dist))