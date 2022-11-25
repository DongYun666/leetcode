# -*- codeing = utf-8 -*-
# @Time : 2021/12/2 20:12
# @Author : DongYun
# @File : 1812.判断国际象棋棋盘中一个格子的颜色.py
# @Software : PyCharm
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        first = ord(coordinates[0])-ord('a')+1
        second = ord(coordinates[1])-ord('1')+1
        return False if (first+second)%2 == 0 else True

    def squareIsWhite2(self, coordinates: str) -> bool:
        return (ord(coordinates[0])+ord(coordinates[1]))%2 == 1

print(Solution().squareIsWhite2("h3"))