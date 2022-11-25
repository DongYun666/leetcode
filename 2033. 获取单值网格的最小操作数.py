# -*- codeing = utf-8 -*-
# @Time : 2021/11/29 21:15
# @Author : DongYun
# @File : 2033. 获取单值网格的最小操作数.py
# @Software : PyCharm
from typing import List
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        ret, li = 0, []
        for i in grid:
            li.extend(i)
        li.sort()
        mid = li[len(li) // 2]
        for v in li:
            if abs(mid - v) % x:
                return -1
            ret += abs(mid - v) // x
        return ret

print(Solution().minOperations([[1,5],[2,3]],2))