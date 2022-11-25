from typing import List
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = []
        for i in range(len(mat[0]),-1,-1):
            for j in range(i,len())





mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
print(Solution().diagonalSort(mat))