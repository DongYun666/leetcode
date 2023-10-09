from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            alive = True
            while alive and asteroid < 0 and stack and stack[-1] > 0:
                alive = stack[-1] < -asteroid
                if stack[-1] <= -asteroid:
                    stack.pop()
            if alive:
                stack.append(asteroid)
        return stack
    
asteroids = [5,10,-5]

asteroids = [10,2,-5]

asteroids = [-2,-1,1,2]

asteroids = [8,-8]

# asteroids = [-2,1,1,-1]
print(Solution().asteroidCollision(asteroids))