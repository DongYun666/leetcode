from typing import List
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        temp = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                temp.append((i+j,j,nums[i][j]))
        temp.sort()
        return [x[2] for x in temp]
nums = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().findDiagonalOrder(nums))