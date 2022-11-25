# -*- codeing = utf-8 -*-
# @Time : 2022/7/21 15:14
# @Author : DongYun
# @File : 911.在线选举.py
# @Software : PyCharm
from bisect import bisect
from collections import defaultdict
from typing import List
class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        temp = defaultdict(int)
        temp[persons[0]]=1
        tops = [persons[0]]
        top = persons[0]
        for p in persons[1:]:
            temp[p]+=1
            if temp[p]>=temp[top]:
                top = p
            tops.append(top)
        self.tops = tops
        self.times = times
    def q(self, t: int) -> int:
        res = bisect(self.times,t)-1
        return self.tops[res]


if __name__ == "__main__":
    t = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    # [3], [12], [25], [15], [24], [8]
    for i in [3,12,25,15,24,8]:
        print(t.q(i))