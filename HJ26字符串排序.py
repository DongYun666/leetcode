# -*- codeing = utf-8 -*-
# @Time : 2022/4/11 20:18
# @Author : DongYun
# @File : HJ26字符串排序.py
# @Software : PyCharm
# A Famous Saying: Much Ado About Nothing (2012/8).
s = input()
record = "" #统计
res = ""
index = 0
for ch in s:
    if ch.isalpha():
        record+=ch
record = sorted(record,key=str.lower)
for i in range(len(s)):
    if s[i].isalpha():
        res+=record[index]
        index+=1
    else:
        res+=s[i]
print(res)
