from typing import List
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m,n = len(rowSum),len(colSum)
        res = [[0]*n for _ in range(m)]
        i = j = 0
        while i < m and j < n:
            v = min(rowSum[i],colSum[j])
            res[i][j] = v
            rowSum[i] -= v
            colSum[j] -= v
            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1
        return res
rowSum = [3,8]
colSum = [4,7]
print(Solution().restoreMatrix(rowSum, colSum))
