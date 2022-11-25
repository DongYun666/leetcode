# -*- codeing = utf-8 -*-
# @Time : 2022/7/13 8:53
# @Author : DongYun
# @File : 735.行星碰撞.py
# @Software : PyCharm
from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        asteroids_da = []
        asteroids_xiao = []
        for i in asteroids:
            if i > 0:
                asteroids_da.append(i)
            else:
                asteroids_xiao.append(i)
        asteroids_da.sort()
        asteroids_xiao.sort(reverse=True)
        max_asteroid_da = asteroids_da[-1]
        max_asteroid_xiao = asteroids_xiao[-1]
        result = []
        if max_asteroid_da == abs(max_asteroid_xiao):
            return []
        if max_asteroid_da > abs(max_asteroid_xiao):
            for i in range(len(asteroids_da)-1,-1,-1):
                if asteroids_da[i]>abs(max_asteroid_xiao):
                    result.append(asteroids_da[i])
        else:
            for i in range(len(asteroids_xiao)-1,-1,-1):
                if abs(asteroids_xiao[i]) > max_asteroid_da:
                    result.append(asteroids_xiao[i])
        return result


asteroids = [10, 2, -5]

print(Solution().asteroidCollision(asteroids))