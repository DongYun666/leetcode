from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 1,max(piles)
        def check(x):
            temp = []
            for pile in piles:
                if pile % x == 0 and pile >= x:
                    temp.append(pile//x)
                else:
                    temp.append(pile//x + 1)
            return sum(temp) > h
        while left < right:
            middle = (left + right) // 2
            if check(middle):
                left = middle+1
            else:
                right = middle
        return left


piles = [3,6,7,11]
h = 8






piles = [30,11,23,4,20]
h = 6
print(Solution().minEatingSpeed(piles, h))
