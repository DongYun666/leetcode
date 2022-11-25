# -*- codeing = utf-8 -*-
# @Time : 2022/4/13 21:58
# @Author : DongYun
# @File : HJ21 简单密码.py
# @Software : PyCharm

s = input()
dict = ['2','2','2','3','3','3','4','4','4','5','5','5','6','6','6','7','7','7','7','8','8','8','9','9','9','9']
# print(len(dict))
res = ""
for ch in s:
    if ch.isalpha():
        if ch.upper() == ch:
            res+=chr((ord(ch.lower())-ord("a")+1)%26+ord("a"))
        if ch.lower() == ch:
            res+=dict[ord(ch)-ord("a")]
    else:
        res+=ch
print(res)