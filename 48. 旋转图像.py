from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        print(matrix)     


matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(Solution().rotate(matrix))