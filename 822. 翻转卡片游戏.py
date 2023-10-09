from typing import List
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)
        same = [fronts[i] for i in range(n) if fronts[i] == backs[i]]
        if len(same) == n:
            return 0
        res = float('inf')
        for front,back in list(zip(fronts,backs)):
            if front not in same:
                res =  min(res,front)
            if back not in same:
                res = min(res,back)
        return res

fronts = [1,2,4,4,7]
backs = [1,3,4,1,3]
print(Solution().flipgame(fronts,backs))