# -*- codeing = utf-8 -*-
# @Time : 2022/4/15 20:49
# @Author : DongYun
# @File : HJ38  求小球落地5次后所经历的路程和第5次返回的高度.py
# @Software : PyCharm

high = float(input())
distance = 0
for i in range(4):
    distance+=(1.5*high)
    high/=2
distance+=high
print(distance)
print(high/2)