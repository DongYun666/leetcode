from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        record = []
        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    record.append((i,j))
        for i,j in record:
            for k in range(m):
                matrix[k][j] = 0
            for k in range(n):
                matrix[i][k] = 0
        print(matrix)



matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]
print(Solution().setZeroes(matrix))