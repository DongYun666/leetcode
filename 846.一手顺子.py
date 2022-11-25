# -*- codeing = utf-8 -*-
# @Time : 2022/3/24 17:30
# @Author : DongYun
# @File : 846.一手顺子.py
# @Software : PyCharm
from collections import Counter
from typing import List
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0:
            return False
        hand.sort()
        cnt = Counter(hand)
        for x in hand:
            if cnt[x] == 0:
                continue
            for num in range(x, x + groupSize):
                if cnt[num] == 0:
                    return False
                cnt[num] -= 1
        return True


hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
print(Solution().isNStraightHand(hand,groupSize))
