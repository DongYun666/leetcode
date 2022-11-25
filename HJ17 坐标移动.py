# -*- codeing = utf-8 -*-
# @Time : 2022/4/15 19:37
# @Author : DongYun
# @File : HJ17 坐标移动.py
# @Software : PyCharm


str_list = input().split(';')
left_right,up_down = 0,0
for s in str_list:
    if 2<= len(s) <= 3 and s[0].isalpha() and s[1:len(s)].isdigit():
        if s[0] == "A":
            left_right-=int(s[1:3])
        elif s[0] == "D":
            left_right+=int(s[1:3])
        elif s[0] == "S":
            up_down-=int(s[1:3])
        elif s[0] == "W":
            up_down+=int(s[1:3])
print(str(left_right)+","+str(up_down))
# A10;S20;W10;D30;X;A1A;B10A11;;A10;