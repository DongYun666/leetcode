# -*- codeing = utf-8 -*-
# @Time : 2022/4/15 21:25
# @Author : DongYun
# @File : HJ9 提取不重复的数.py
# @Software : PyCharm

s = list(input())
res = ""
for ch in s[::-1]:
    if ch not in res:
        res+=ch
print(res)
