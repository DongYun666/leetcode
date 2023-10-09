from typing import List
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res = 0
        temp = capacity
        for index,plant in enumerate(plants):
            if plant > temp:
                res += 2*index+1
                temp = capacity - plant
            else:
                temp -= plant
                res += 1
        return res
plants = [2,2,3,3]
capacity = 5

plants = [1,1,1,4,2,3]
capacity = 4

plants = [7,7,7,7,7,7,7]
capacity = 8
print(Solution().wateringPlants(plants, capacity))