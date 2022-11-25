# -*- codeing = utf-8 -*-
# @Time : 2022/4/13 20:09
# @Author : DongYun
# @File : HJ20 密码验证合格程序.py
# @Software : PyCharm

def check(s:str):
    if len(s)<=8:
        return False
    type = []
    for index,ch in enumerate(s):
        if ch.isalpha():
            if ch.lower() == ch and "lower" not in type:
                type.append("lower")
            if ch.upper() == ch and "upper" not in type:
                type.append("upper")
        elif ch.isdigit():
            if "digit" not in type:
                type.append("digit")
        else:
            if "other" not in type:
                type.append("other")
        if index+2<=len(s):
            if s[index:index+3] in s[index+3:]:
                return False
    if len(type) <= 2:
        return False
    return True
while True:
    try:
        s = input()
        print("OK" if check(s) else "NG")
    except:
        break