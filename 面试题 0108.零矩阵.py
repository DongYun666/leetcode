from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = [False] * len(matrix)
        col = [False] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] or col[j]:
                    matrix[i][j] = 0
        return matrix





matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
print(Solution().setZeroes(matrix))