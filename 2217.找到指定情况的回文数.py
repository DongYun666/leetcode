# -*- codeing = utf-8 -*-
# @Time : 2022/4/6 20:29
# @Author : DongYun
# @File : 2217.找到指定情况的回文数.py
# @Software : PyCharm
import math
from typing import List
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        temp = []
        res = []
        num = 10**(math.ceil(intLength /2) -1)
        for x in queries:
            if x > 10**intLength:
                temp.append(-1)
                continue
            temp.append(num+x-1)
        print(temp)
        if intLength%2:
            print("************************")
            for x in temp:
                if x == -1:
                    res.append(-1)
                    continue
                y = x//10
                x = x * 10 ** (math.ceil(intLength / 2)-1)
                wei = num//10
                while y != 0:
                    x += (y % 10) * wei
                    y //= 10
                    wei //= 10
                if x > 10 ** intLength:
                    res.append(-1)
                else:
                    res.append(x)
        else:   #偶数位
            for x in temp:
                if x == -1:
                    res.append(-1)
                    continue
                y = x
                x = x*10**(math.ceil(intLength/2))
                wei = num
                while y != 0:
                    x+=(y%10)*wei
                    y //=10
                    wei //=10
                if x > 10 ** intLength:
                    res.append(-1)
                else:
                    res.append(x)
        return res
queries = [94,18,388481008,38,16017953,16,223505660,78,123699557,346244579,2]
intLength = 8
print(Solution().kthPalindrome(queries,intLength))