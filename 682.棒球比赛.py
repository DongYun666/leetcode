# -*- codeing = utf-8 -*-
# @Time : 2022/3/26 8:21
# @Author : DongYun
# @File : 682.棒球比赛.py
# @Software : PyCharm

from typing import List
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        temp = []
        index = -1
        for x in ops:
            if x == "C":
                if len(temp)!=0:
                    temp.pop()
                    index-=1
            elif x == "D":
                if len(temp)!=0:
                    temp.append(temp[index]*2)
                    index+=1
            elif x == "+":
                if len(temp)>=2:
                    temp.append(temp[index]+temp[index-1])
                    index+=1
            else:
                    temp.append(int(x))
                    index += 1
        return sum(temp)

    def calPoints1(self, ops: List[str]) -> int:
        ans = 0
        points = []
        for op in ops:
            if op == '+':
                pt = points[-1] + points[-2]
            elif op == 'D':
                pt = points[-1] * 2
            elif op == 'C':
                ans -= points.pop()
                continue
            else:
                pt = int(op)
            ans += pt
            points.append(pt)
        return ans


ops = ["5","2","C","D","+"]
print(Solution().calPoints(ops))