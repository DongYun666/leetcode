from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(i, target, path):
            if target == 0:
                res.append(path)
                return
            if i == n or target < 0:
                return
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                dfs(j + 1, target - candidates[j], path + [candidates[j]])

        candidates.sort()
        n = len(candidates)
        res = []
        dfs(0, target, [])
        return res
candidates = [10,1,2,7,6,1,5]
target = 8
print(Solution().combinationSum2(candidates, target))
