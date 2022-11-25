# -*- codeing = utf-8 -*-
# @Time : 2022/4/12 22:31
# @Author : DongYun
# @File : HJ36 字符串解密.py
# @Software : PyCharm

key = str(input())
plain = str(input())
key_temp = ""
for k in key:
    if k not in key_temp:
        key_temp+=k
key = key_temp
miwen = []
for k in key:
    miwen.append(k)
for i in range(0,26):
    if chr(ord("a")+i) not in key:
        miwen.append(chr(ord("a")+i))
for c in plain:
    print(miwen[ord(c)-ord("a")],end="")




# print(key)
# cipher