# -*- codeing = utf-8 -*-
# @Time : 2022/7/21 11:51
# @Author : DongYun
# @File : 剑指Offer 66.构建乘积数组.py
# @Software : PyCharm
from typing import List
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        res = []
        temp = 1
        for x in a:
            if x == 0:
                continue
            temp*=x
        for x in a:
            if x == 0:
                res.append(x)
                continue
            res.append(int(temp/x))
        return res

a = [1,2,0,4,5]
print(Solution().constructArr(a))
