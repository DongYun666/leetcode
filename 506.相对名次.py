# -*- codeing = utf-8 -*-
# @Time : 2021/12/2 19:50
# @Author : DongYun
# @File : 506.相对名次.py
# @Software : PyCharm
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        resoult = []
        temp = score.copy()
        temp.sort(reverse=True)
        for num in score:
            index = temp.index(num)
            if index == 0:
                resoult.append("Gold Medal")
            elif index == 1:
                resoult.append("Silver Medal")
            elif index == 2:
                resoult.append("Bronze Medal")
            else:
                resoult.append(str(index+1))
        return resoult
    def findRelativeRanks2(self, score: List[int]) -> List[str]:
        record = {}
        for index,num in enumerate(score):
            record[num]=index
        score.sort(reverse=True)
        res = [0] * len(score)
        title = ["Gold Medal","Silver Medal","Bronze Medal"]
        for i,v in enumerate(score):
            if i < 3:
                res[record[v]] = title[i]
            else:
                res[record[v]] = str(i+1)
        return res

print(Solution().findRelativeRanks2([10,3,8,9,4]))
