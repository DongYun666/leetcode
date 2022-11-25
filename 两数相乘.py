# -*- codeing = utf-8 -*-
# @Time : 2021/11/8 14:58
# @Author : DongYun
# @File : 两数相乘.py
# @Software : PyCharm
def getSum( a: int, b: int) -> int:
    # if a < 0 and b > 0:
    #     b = ~b + 1
    # if b < 0 and a > 0:
    #     b = ~b + 1
    while b != 0:
        a, b = a ^ b, (a & b) << 1
    return a
def multi(a,b):
    res = 0
    while b != 0:
        if b&1 != 0:
            res = getSum(res,a)
        a <<=1
        b >>=1
    return  res
print(multi(10,7))