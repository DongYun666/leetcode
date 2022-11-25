from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1],reverse=True)
        res = 0
        for numberOfBoxes,numberOfUnitsPerBox in boxTypes:
            if numberOfBoxes>=truckSize:
                res+=truckSize*numberOfUnitsPerBox
                return res
            res+=numberOfBoxes*numberOfUnitsPerBox
            truckSize-=numberOfBoxes

boxTypes = [[1, 3], [2, 2], [3, 1]]
truckSize = 4

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
print(Solution().maximumUnits(boxTypes, truckSize))