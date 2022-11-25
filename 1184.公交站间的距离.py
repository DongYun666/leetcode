# -*- codeing = utf-8 -*-
# @Time : 2022/7/24 18:34
# @Author : DongYun
# @File : 1184.公交站间的距离.py
# @Software : PyCharm
from typing import List
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        distance_sum = sum(distance)
        temp_sum = 0
        while start%len(distance) != destination:
            if start>=len(distance):
                start %= len(distance)
            temp_sum += distance[start]
            start+=1
        return min(temp_sum,distance_sum-temp_sum)

distance = [1,2,3,4]
start = 0
destination = 3
print(Solution().distanceBetweenBusStops(distance,start,destination))

