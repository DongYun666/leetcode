from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        res = []
        i,j = 0,0
        while i < m and j < n:
            for k in range(j,n):
                res.append(matrix[i][k])
            i += 1
            for k in range(i,m):
                res.append(matrix[k][n-1])
            n -= 1
            if i < m:
                for k in range(n-1,j-1,-1):
                    res.append(matrix[m-1][k])
                m -= 1
            if j < n:
                for k in range(m-1,i-1,-1):
                    res.append(matrix[k][j])
                j += 1
        return res
    
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(Solution().spiralOrder(matrix))