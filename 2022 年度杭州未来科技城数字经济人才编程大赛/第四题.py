# -*- codeing = utf-8 -*-
# @Time : 2022/7/8 12:59
# @Author : DongYun
# @File : 第四题.py
# @Software : PyCharm
from typing import List
class Solution:
    def minTransfers(self, distributions: List[List[int]]) -> int:
        stros = [0 for i in range(12)]
        for x in distributions:
            stros[x[0]] -= x[2]
            stros[x[1]] += x[2]
        count = 0
        da = []
        xiao = []
        print(stros)
        for x in stros:
            if x > 0:
                da.append(x)
            elif x < 0:
                xiao.append(abs(x))
        for da_i in range(len(da)):
            if da[da_i] in xiao:
                xiao[xiao.index(da[da_i])] = 0
                da[da_i] = 0
                count+=1
        da.remove(0)
        da.sort(reverse=True)
        print(da)
        xiao.sort(reverse=True)
        print(xiao)

        for i in range(len(da)):
            for j in range(len(xiao)):
                if xiao[j]==0:
                    continue
                else:
                    if da[i] > xiao[j]:
                        da[i]-=xiao[j]
                        xiao[j]=0
                        count+=1
                    else:
                        xiao[j]-=da[i]
                        count+=1
        return count
        # print(stros,count,da,xiao)
#

distributions = [[1,5,8],[8,9,8],[2,3,9],[4,3,1]]
print(Solution().minTransfers(distributions))