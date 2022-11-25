# -*- codeing = utf-8 -*-
# @Time : 2022/4/11 21:30
# @Author : DongYun
# @File : HJ57高精度加法.py
# @Software : PyCharm

str1 = input()
str2 = input()
if len(str1) > len(str2):
    str1,str2 = str2,str1
res= ""
temp = 0
wei = 0
for i in range(len(str2)-1,-1,-1):
    s_1 = int(str1[i-(len(str2)-len(str1))])
    s_2 = int(str2[i])
    temp = s_1+s_2+temp
    res=str(temp%10)+res
    temp //= 10
    wei +=1
    if wei == len(str1):
        break
while wei < len(str2):
    s_2 = int(str2[len(str2)-wei-1])
    temp += s_2
    res=str(temp%10)+res
    wei+=1
    temp //=10
if temp!= 0:
    res=str(temp)+res
    res+=temp*(10**(wei+1))
print(res)
# 9876543210
# 1234567890
