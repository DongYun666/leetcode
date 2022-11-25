# -*- codeing = utf-8 -*-
# @Time : 2022/7/8 10:19
# @Author : DongYun
# @File : 第一题.py
# @Software : PyCharm
from typing import List

class Solution:
    def canReceiveAllSignals(self, intervals: List[List[int]]) -> bool:
        flag = True
        for i in range(len(intervals)):
            for j in range(i+1,len(intervals)):
                if intervals[i][0]<=intervals[j][0]:
                    if intervals[i][1] > intervals[j][0]:
                        flag = False
                        break
                if intervals[i][0]>=intervals[j][0]:
                    if intervals[i][0]<intervals[j][1]:
                        flag = False
                        break
        return flag
signals = [[2,8],[8,14]]
print(Solution().canReceiveAllSignals(signals))