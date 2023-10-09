from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m,n = len(matrix),len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[i][j] = 1 if j == 0 else dp[i][j - 1] + 1

        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    height = 1
                    width = dp[i][j]
                    res = max(res,height * width)
                    for k in range(i-1,-1,-1):
                        if matrix[k][j] == "1":
                            height += 1
                            width = min(width,dp[k][j])
                            res = max(res,height * width)
                        else:
                            break
        return res

matrix = [["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "1", "0"]]
matrix = [["1"]]
matrix = [["0","1"],["1","1"]]
print(Solution().maximalRectangle(matrix))