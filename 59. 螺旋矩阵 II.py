from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = n
        matrix = [[0] * n for _ in range(m)]
        i, j = 0, 0
        m = n
        num = 1
        while i < m and j < n:
            for k in range(j, n):
                matrix[i][k] = num
                num += 1
            i += 1
            for k in range(i, n):
                matrix[k][n - 1] = num
                num += 1
            n -= 1
            if i < m:
                for k in range(n - 1, j - 1, -1):
                    matrix[m - 1][k] = num
                    num += 1
                m -= 1
            if j < n:
                for k in range(m - 1, i - 1, -1):
                    matrix[k][j] = num
                    num += 1
                j += 1
        return matrix
    
n = 3
print(Solution().generateMatrix(n))