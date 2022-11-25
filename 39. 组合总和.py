from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        def dfs(index,s_m):
            if s_m == target:
                t = sorted(temp[:])
                if t not in res:
                    res.append(t[:])
                return
            if s_m>target:
                return
            for i in range(len(candidates)):
                temp.append(candidates[i])
                s_m+=candidates[i]
                dfs(index+1,s_m)
                temp.pop()
                s_m-=candidates[i]
        dfs(0,0)
        return res

candidates = [2,3,5]
target = 8
print(Solution().combinationSum(candidates, target))