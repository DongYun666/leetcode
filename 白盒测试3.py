# -*- codeing = utf-8 -*-
# @Time : 2022/5/4 20:02
# @Author : DongYun
# @File : 白盒测试3.py
# @Software : PyCharm
from random import randint
from typing import List
class SearchBall:
    def search_diff(self,x:List[int]):
        if (sum(x[:5])<sum(x[5:])):
            if x[1]+x[2] == x[3]+x[4]:
                return "1号是假球"
            if x[1] + x[2] < x[3] + x[4]:
                if x[1]<x[2]:
                    return "2号是假球"
                else:
                    return "3号是假球"
            else:
                if x[3]<x[5]:
                    return "4号是假球"
                else:
                    return "5号是假球"
        else:
            if x[6]+x[7] == x[8]+x[9]:
                return "6号是假球"
            if x[6] + x[7] < x[8] + x[9]:
                if x[6]<x[7]:
                    return "7号是假球"
                else:
                    return "8号是假球"
            else:
                if x[8]<x[9]:
                    return "9号是假球"
                else:
                    return "10号是假球"
x = [2,2,2,2,2,2,2,2,2,2]
x[randint(0,9)] = 1
print(x)
print(SearchBall().search_diff(x))


