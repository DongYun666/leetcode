# -*- codeing = utf-8 -*-
# @Time : 2022/5/2 20:23
# @Author : DongYun
# @File : 187.重复得DNA序列.py
# @Software : PyCharm
from collections import defaultdict
from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        tongji = defaultdict()
        for index in range(len(s)-10+1):
            temp = s[index:index+10]
            if temp not in tongji:
                tongji[temp] = 1
            else:
                tongji[temp]+=1
            if tongji[temp] == 2 and temp not in res:
               res.append(temp)
        return res






s = "AAAAAAAAAAAAA"
print(Solution().findRepeatedDnaSequences(s))
