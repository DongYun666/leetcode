# -*- codeing = utf-8 -*-
# @Time : 2022/2/24 15:52
# @Author : DongYun
# @File : 1706. 球会落何处.py
# @Software : PyCharm
from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        ans = [-1]*n
        for j in range(n):
            col = j
            for row in grid:
                dir = row[col]
                col +=dir
                if col <0 or col == n or row[col] != dir:
                    break
            else:    # else 子句在循环正常完成时执行，这意味着循环没有遇到任何 break 语句。
                ans[j] = col
        return ans

        def findBall2(self, grid: List[List[int]]) -> List[int]:
            n = len(grid[0])
            ans = [-1] * n
            for boll in range(n):  # n个小球从顶部放入
                col = boll
                for row in grid:
                    j = row[col]
                    col += j  # 小球向下走
                    if col < 0 or col == n or row[col] != j:  # 边界检测以及“V”字检测
                        break
                else:
                    ans[boll] = col  # 记录小球掉落位置
            return ans

grid = [[1,1,1,1,1,1],
        [-1,-1,-1,-1,-1,-1],
        [1,1,1,1,1,1],
        [-1,-1,-1,-1,-1,-1]]
print(Solution().findBall2(grid))


