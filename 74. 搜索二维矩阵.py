from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            if matrix[i][0] == target:
                return True
            if matrix[i][0] > target:
                break
        if i == 0:
            return False
        i = i - 1
        left,right = 0,n-1
        while left < right:
            mid = (left + right) // 2
            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] > target:
                right = mid
            else:
                left = mid + 1
        return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

matrix = [[1,3]]
target = 3
print(Solution().searchMatrix(matrix, target))