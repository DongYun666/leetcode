# -*- codeing = utf-8 -*-
# @Time : 2022/4/4 19:30
# @Author : DongYun
# @File : 5235.找出输掉零场或一场比赛的玩家.py
# @Software : PyCharm
from collections import defaultdict
from typing import List
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count_loser = defaultdict(int)
        for win,loser in matches:
            if win not in count_loser:
                count_loser[win] = 0
            count_loser[loser] +=1
        answer1 = []
        answer2 = []
        for key,num in count_loser.items():
            if num == 0:
                answer1.append(key)
            if num == 1:
                answer2.append(key)
        return [sorted(answer1),sorted(answer2)]

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(Solution().findWinners(matches))