# -*- codeing = utf-8 -*-
# @Time : 2022/3/31 10:57
# @Author : DongYun
# @File : 面试题 01.08.零矩阵.py
# @Software : PyCharm

from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        temp = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    temp.append((i,j))
        print(temp)
        for t in temp:
            for i in range(len(matrix[0])):
                matrix[t[0]][i] = 0
            for i in range(len(matrix)):
                matrix[i][t[1]] = 0
        return matrix


matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
print(Solution().setZeroes(matrix))