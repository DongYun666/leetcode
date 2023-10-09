from typing import List
class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        # 生成特殊路径的字典
        res = 0
        cur_x, cur_y = start[0], start[1] 
        for x1, y1, x2, y2, cost in specialRoads:
            if cur_x > x2 or cur_y > y2:
                continue
            


        special = []
        for road in range(len(specialRoads)):
            if road[4] > abs(road[0] - road[2]) + abs(road[1] - road[3]) or road[2]< road[0] or road[3] < road[1]:
                continue
            else:
                special.append(road)
        special = sorted(special,key=lambda x:x[0])

        
        