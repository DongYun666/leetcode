# -*- codeing = utf-8 -*-
# @Time : 2022/7/10 10:20
# @Author : DongYun
# @File : 第三题.py
# @Software : PyCharm
from typing import List
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_temp,target_temp = "",""
        start_index,target_index = [],[]
        for i in range(len(start)):
            if start[i] != "_":
                start_temp+=start[i]
                start_index.append(i)
            if target[i] != "_":
                target_temp+=target[i]
                target_index.append(i)
        if start_temp != target_temp:
            return False
        for i in range(len(start_temp)):
            if target_temp[i] == "L" and target_index[i]>start_index[i]:
                return False
            if target_temp[i] == "R" and target_index[i]<start_index[i]:
                return False
        return True



start = "_L__R__R_"
target = "L______RR"
print(Solution().canChange(start,target))