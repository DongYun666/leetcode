from typing import List

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        max_x = max(t[0] for t in towers)
        max_y = max(t[1] for t in towers)
        rx,ry,max_qual = 0,0,0
        for x in range(max_x+1):
            for y in range(max_y+1):
                qual = 0
                for tx,ty,p in towers:
                    dis = (tx-x)**2+(ty-y)**2
                    if dis <= radius**2:
                        qual += int(p/(1+dis**0.5))
                if qual > max_qual:
                    rx,ry,max_qual = x,y,qual
        return [rx,ry]


towers = [[1, 2, 5], [2, 1, 7], [3, 1, 9]]
radius = 2

towers = [[1,2,13],[2,1,7],[0,1,9]]
radius = 2
print(Solution().bestCoordinate(towers, radius))