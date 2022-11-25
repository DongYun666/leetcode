# -*- codeing = utf-8 -*-
# @Time : 2022/2/20 10:23
# @Author : DongYun
# @File : 717.1比特与2比特字符.py
# @Software : PyCharm
from typing import List
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        index,lenth = 0,len(bits)
        while index < lenth-1:
            if bits[index] == 1:
                index +=2
            else:
                index +=1
        return index == lenth -1




bits = [0,0,0]
print(Solution().isOneBitCharacter(bits))