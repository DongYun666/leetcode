from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def reverse_matrix(m):
            if not m:
                return []
            return [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))][::-1]
        res = []
        while matrix:
            res+=matrix.pop(0)
            matrix = reverse_matrix(matrix)
        return res

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().spiralOrder(matrix))
