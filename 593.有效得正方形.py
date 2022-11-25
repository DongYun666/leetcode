# -*- codeing = utf-8 -*-
# @Time : 2022/7/29 12:18
# @Author : DongYun
# @File : 593.有效得正方形.py
# @Software : PyCharm
from math import sqrt
from typing import List
class Solution:
    def count_length(self,x,y):
        return sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        temp = []
        temp.append(self.count_length(p1,p2))
        temp.append(self.count_length(p1,p3))
        temp.append(self.count_length(p1,p4))
        temp.append(self.count_length(p2,p3))
        temp.append(self.count_length(p2,p4))
        temp.append(self.count_length(p3,p4))
        temp.sort()
        if temp[0] == temp[1] == temp[2] == temp[3] and temp[4] == temp[5]:
            return True
        else:
            return False




p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,12]
print(Solution().validSquare(p1,p2,p3,p4))