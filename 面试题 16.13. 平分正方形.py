from typing import List
class Solution:
    def min_max(self,nums):
        min_nums = float("inf")
        max_nums = float("-inf")
        for i in nums:
            if i <= 0:
                min_nums = min(min_nums,i)
            else:
                max_nums = max(max_nums,i)
            return [min_nums,max_nums]
    def cutSquares(self, square1: List[int], square2: List[int]) -> List[float]:
        square1_center = [square1[0]+square1[2]/2,square1[1]+square1[2]/2]
        square2_center = [square2[0]+square2[2]/2,square2[1]+square2[2]/2]
        if square1_center[0]-square2_center[0] == 0:
            slope = float("inf")
        else:
            slope = (square2_center[1]-square1_center[1])/(square2_center[0]-square1_center[0])
        square1_2_x = self.min_max([square1[0],square1[0]+square1[2],square2[0],square2[0]+square2[2]])
        square1_2_y = self.min_max([square1[1],square1[1]+square1[2],square2[1],square2[1]+square2[2]])
        print(square1_2_x,square1_2_y)



square1 = [-1, -1, 2]
square2 = [0, -1, 2]
print(Solution().cutSquares(square1,square2))