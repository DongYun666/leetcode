from typing import List
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        pre_0 = [0]*(n+1)
        pre_1 = [0]*(n+1)

        for i in range(n):
            pre_0[i+1] = pre_0[i] + grid[0][i]
            pre_1[i+1] = pre_1[i] + grid[1][i]
        res = float("inf")
        for i in range(n):
            res = min(res,max(pre_0[-1]-pre_0[i+1],pre_1[i]))
        return res      
grid = [[2,5,4],[1,5,1]]
# grid = [[3,3,1],[8,5,2]]
print(Solution().gridGame(grid))