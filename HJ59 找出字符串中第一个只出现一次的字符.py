# -*- codeing = utf-8 -*-
# @Time : 2022/4/16 20:02
# @Author : DongYun
# @File : HJ59 找出字符串中第一个只出现一次的字符.py
# @Software : PyCharm
while True:
    try:
        s = input()
        for i in s:
            if s.count(i) == 1:
                print(i)
                break
        else:
            print('-1')
    except:
        break