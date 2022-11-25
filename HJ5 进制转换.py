# -*- codeing = utf-8 -*-
# @Time : 2022/4/11 22:33
# @Author : DongYun
# @File : HJ5 进制转换.py
# @Software : PyCharm


s = input()[2:]
res = 0
wei = 0
for index in range(len(s)-1,-1,-1):
    if s[index].isalpha():
        res+=(ord(s[index])-ord("A")+10)*(16**wei)
        wei+=1
    else:
        res+=int(s[index])*(16**wei)
        wei+=1
print(res)