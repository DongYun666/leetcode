# -*- codeing = utf-8 -*-
# @Time : 2022/4/13 22:11
# @Author : DongYun
# @File : HJ22.py
# @Software : PyCharm

while True:
    try:
        x = int(input())
        if x == 0:
            break
        res = x//3
        x = x%3
        he = res+x
        while x != 1:

        print(res)
    except:
        break