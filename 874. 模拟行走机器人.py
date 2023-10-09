from typing import List
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        res,x,y = 0,0,0
        obstacles = set(map(tuple, obstacles))
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        direction = 1
        for command in commands:
            if command < 0:
                direction += 1 if command == -1 else -1 
                direction %= 4
            else:
                for _ in range(command):
                    if (x + directions[direction][0], y + directions[direction][1]) not in obstacles:
                        x += directions[direction][0]
                        y += directions[direction][1]
                        res = max(res, x**2 + y**2)
        return res
    

commands = [4,-1,4,-2,4]
obstacles = [[2,4]]
print(Solution().robotSim(commands, obstacles))