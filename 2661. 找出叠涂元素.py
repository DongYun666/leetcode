from collections import defaultdict
from typing import List
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        dect = defaultdict(list)
        m,n = len(mat),len(mat[0])
        for i in range(m):
            for j in range(n):
                dect[mat[i][j]].append(i)
                dect[mat[i][j]].append(j)
        row,col = [0] * m,[0] * n
        for i in range(len(arr)):
            r,c= dect[arr[i]]
            row[r] += 1
            col[c] += 1
            if row[r] == n or col[c] == m:
                return i
        return -1
arr = [1,3,4,2]
mat = [[1,4],[2,3]]

# arr = [1,4,5,2,6,3]
# mat = [[4,3,5],[1,2,6]]

arr = [2,8,7,4,1,3,5,6,9]
mat = [[3,2,5],[1,4,6],[8,7,9]]
print(Solution().firstCompleteIndex(arr, mat))