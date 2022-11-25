# -*- codeing = utf-8 -*-
# @Time : 2022/4/12 9:36
# @Author : DongYun
# @File : HJ6 质数因子.py
# @Software : PyCharm

res = []
for i in range(2,2*(10**9)+13):
    flag = True
    for j in range(2,i):
        if i % j !=0:
            flag = False
    if flag:
        res.append(i)
print(res)