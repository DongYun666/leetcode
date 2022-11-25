from typing import List
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0
        row_1_count = [row.count(1) for row in mat]
        col_1_count = [col.count(1) for col in zip(*mat)]
        for i in range(len(row_1_count)):
            if row_1_count[i] == 1:
                col = mat[i].index(1)
                if col_1_count[col] == 1:
                    res+=1
        return res

mat = [[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,1],[0,0,0,0,1,0,0,0],[1,0,0,0,1,0,0,0],[0,0,1,1,0,0,0,0]]
print(Solution().numSpecial(mat))

