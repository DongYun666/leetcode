from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        for i in range(1,len(grid)):
            for j in range(len(grid[0])):
                min_num = float("inf")
                for k in range(len(grid[0])):
                    if k==j:
                        continue
                    else:
                        min_num = min(min_num,grid[i-1][k])
                grid[i][j] += min_num
        return min(grid[-1])

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr = [[-73,61,43,-48,-36],
       [3,30,27,57,10],
       [96,-76,84,59,-15],
       [5,-49,76,31,-7],
       [97,91,61,-46,67]]

print(Solution().minFallingPathSum(arr))