import bisect
from typing import List
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans = float("-inf")
        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            total = [0] * n
            for j in range(i,m):
                for c in range(n):
                    total[c] += matrix[j][c]
                s = 0
                total_set = [0]
                for v in total:
                    s += v
                    lb = bisect.bisect_left(total_set,s-k)
                    if lb != len(total_set):
                        ans = max(ans,s-total_set[lb])
                    total_set.append(s)
                    total_set.sort()
        return ans
    
matrix = [[1,0,1],[0,-2,3]]
k = 2

matrix = [[5,-4,-3,4],
          [-3,-4,4,5],
          [5,1,5,-4]]
k = 10
print(Solution().maxSumSubmatrix(matrix,k))