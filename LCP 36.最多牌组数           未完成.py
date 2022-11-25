# -*- codeing = utf-8 -*-
# @Time : 2021/12/4 14:41
# @Author : DongYun
# @File : LCP 36.最多牌组数.py
# @Software : PyCharm
from collections import Counter
from typing import List
class Solution:
    def maxGroupNumber(self, tiles: List[int]) -> int:
        tiles_Counter = Counter(tiles)
        for i in sorted(tiles_Counter):
            print(i)
        # if len(tiles)<4:
        #     return 0
        # for tile in tiles:
        #     print(tile)

        return 0

print(Solution().maxGroupNumber([2,2,2,3,4,1,3]))

