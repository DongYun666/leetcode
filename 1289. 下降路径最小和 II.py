from typing import List
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(n):
            dp[0][i] = grid[0][i]
        for i in range(1,m):
            for j in range(n):
                dp[i][j] = min([num for index,num in enumerate(dp[i-1]) if index != j]) + grid[i][j]
                    # min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1]) + grid[i][j]
        return min(dp[-1])
    
grid = [[2,1,3],[6,5,4],[7,8,9]]
# grid = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().minFallingPathSum(grid))