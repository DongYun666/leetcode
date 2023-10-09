from typing import List
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left,right = 0, max(ranks)*cars*cars

        def check(ranks, cars, mid):
            cnt = 0
            for rank in ranks:
                cnt += int((mid / rank) ** 0.5)
            return cnt >= cars
        
        while left < right:
            mid = (left+right)//2
            if check(ranks, cars, mid):
                right = mid
            else:
                left = mid+1
        
        return left


ranks = [4,2,3,1]
cars = 10

ranks = [5,1,8]
cars = 6
print(Solution().repairCars(ranks, cars))