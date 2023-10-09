from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        row_sum = [sum(grid[i][j] for j in range(3)) for i in range(3)]
        col_sum = [sum(grid[j][i] for i in range(3)) for j in range(3)]
        dig_sum = [grid[0][0]+grid[1][1]+grid[2][2],grid[0][2]+grid[1][1]+grid[2][0],grid[0][2]+grid[1][1]+grid[2][0]]
        res = 0
        for i in range(len(grid)-3):
            for j in range(len(grid[0])-3):
                row_sum[0] = row_sum[0]-grid[]




        print(row_sum)
        print(col_sum)
        print(dig_sum)






grid = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]
print(Solution().numMagicSquaresInside(grid))