# -*- codeing = utf-8 -*-
# @Time : 2022/4/16 19:31
# @Author : DongYun
# @File : HJ55 挑7.py
# @Software : PyCharm


x = int(input())
count = 0
def han_7(x):
    while x!= 0:
        temp = x%10
        if temp == 7:
            return True
        x=x//10
    return False
for i in range(1,x+1):
    if i % 7 ==0:
        count+=1
        print(i)
    elif han_7(i):
        print(i)
        count+=1
print(count)

