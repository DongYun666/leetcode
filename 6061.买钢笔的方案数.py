# -*- codeing = utf-8 -*-
# @Time : 2022/4/17 18:46
# @Author : DongYun
# @File : 6061.买钢笔的方案数.py
# @Software : PyCharm

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        res = 0
        for i in range(0,total//cost1+1):
            res+=((total-i*cost1)//cost2)+1
        return res


total = 5
cost1 = 10
cost2 = 10
print(Solution().waysToBuyPensPencils(total,cost1,cost2))


