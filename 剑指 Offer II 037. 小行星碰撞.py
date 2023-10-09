from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for asteroid in asteroids:
            if asteroid > 0:
                res.append(asteroid)
            else:
                while res and res[-1] > 0 and res[-1] < -asteroid:
                    res.pop()
                if not res or res[-1] < 0:
                    res.append(asteroid)
                elif res[-1] == -asteroid:
                    res.pop()
        return res
asteroids = [5,10,-5]
asteroids = [8,-8]
asteroids = [10,2,-5]
asteroids = [-2,-1,1,2]
print(Solution().asteroidCollision(asteroids))