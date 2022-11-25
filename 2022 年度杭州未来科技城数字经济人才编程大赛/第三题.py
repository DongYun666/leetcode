# -*- codeing = utf-8 -*-
# @Time : 2022/7/8 11:21
# @Author : DongYun
# @File : 第三题.py
# @Software : PyCharm
from typing import List
class Solution:
    def buildTransferStation(self, area: List[List[int]]) -> int:
        x,y = [],[]
        for i in range(len(area)):
            for j in range(len(area[0])):
                if area[i][j] == 1:
                    x.append(i)
                    y.append(j)
        x.sort()
        y.sort()
        ans = 0
        for i in range(len(x)):
            ans +=abs(x[i]-x[len(x)//2])+abs(y[i]-y[len(y)//2])
        return ans
        # print(x,y)
        # x = int(x_sum/count)
        # y = int(y_sum/count)
        # ans = 0
        # for res in resoult:
        #     ans += abs(x-res[0])
        #     ans += abs(y-res[1])
        # return  ans

area = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,1,0],[1,1,0,0,0,0,1,0,0],[0,0,0,1,1,1,0,0,0]]
print(Solution().buildTransferStation(area))