# -*- codeing = utf-8 -*-
# @Time : 2022/7/14 10:42
# @Author : DongYun
# @File : ipc2_6 点名.py
# @Software : PyCharm

n,m = list(map(int,input().split()))
_ = input()
duiwu = list(map(int,input().split()))
_ = input()
dianming = list(map(int,input().split()))
top = 0
result = []
for i in dianming:
    temp = duiwu[:i]
    temp.sort()
    # result.append(temp[top] if top<len(temp) else temp[-1])
    result.append(temp[top])
    top +=1
for res in result:
    print(res)

# 7 4
# 9 7 2 8 14 1 8
# 1 2 6 6