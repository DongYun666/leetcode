from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:  # 边界条件，当起点与终点有障碍物时，直接返回0
            return 0
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        for i in range(len(dp)):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = 1
            else:
                break
        for j in range(len(dp[0])):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = 1
            else:
                break
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j]
        return dp[-1][-1]
        print(dp)



obstacleGrid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))