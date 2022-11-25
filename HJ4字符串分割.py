# -*- codeing = utf-8 -*-
# @Time : 2022/4/12 9:13
# @Author : DongYun
# @File : HJ4字符串分割.py
# @Software : PyCharm
while True:
    try:
        s = input()
        n = len(s)
        s += "0"*(8-n%8)
        n+=(8-n%8)
        for i in range(0,n,8):
            print(s[i:i+8])
    except:
        break