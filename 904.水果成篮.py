from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket1,basket2 = -1,-1
        res = 0
        left = 0
        for right in range(len(fruits)):
            if basket1 == -1 or basket1 == fruits[right]:
                basket1 = fruits[right]
                continue
            if basket2 == -1 or basket2 == fruits[right]:
                basket2 = fruits[right]
                continue
            if basket1 != fruits[right] and basket2 != fruits[right]:
                res = max(res,right-left)
                left = right-1
                while fruits[left] == fruits[left-1]:
                    left -=1
                if basket1 != fruits[left]:
                    basket1 = fruits[right]
                elif basket2 !=fruits[left]:
                    basket2 =fruits[right]
        return max(res,right-left+1)


fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
# fruits = [1,2,3,2,2]
# fruits = [0,1,2,2]
print(Solution().totalFruit(fruits))