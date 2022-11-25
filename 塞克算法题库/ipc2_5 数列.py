# -*- codeing = utf-8 -*-
# @Time : 2022/7/14 9:38
# @Author : DongYun
# @File : ipc2_5 数列.py
# @Software : PyCharm

# n = int(input())
# num = list(map(int,input().split()))
# Last = 0
# result = []
# for _ in range(n):
#     a,b,c = list(map(int,input().split()))
#     a += Last
#     b += Last
#     c += Last
#     if a == 0 and b==0 and c==0:
#         break
#     l,r = 0,len(num)-1
#     while l <= r:
#         mid = (l+r)//2
#         if a*(mid+2)*num[mid]**2+(b+1)*(mid+1)*num[mid]+(c+mid+1) == 0:
#             Last = mid+1
#             result.append(mid+1)
#             break
#         else:
#             if 2*a*(mid+2)*num[mid]+(b+1)*(mid+1) > 0:
#                 if (a * (mid + 2) * num[mid] ** 2 + (b + 1) * (mid + 1) * num[mid] + (c + mid + 1)) > 0:
#                     r = mid -1
#                 else:
#                     l = mid+1
#             elif 2*a*(mid+2)*num[mid]+(b+1)*(mid+1) < 0:
#                 if (a * (mid + 2) * num[mid] ** 2 + (b + 1) * (mid + 1) * num[mid] + (c + mid + 1)) > 0:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
# for i in result:
#     print(i)
    # for i in range(len(num)):
    #     if a*(i+2)*num[i]**2+(b+1)*(i+1)*num[i]+(c+i+1) == 0:
    #         Last = i+1
    #         print(i+1)
    #         break

n = int(input())
num = list(map(int,input().split()))
a,b,c = [],[],[]
for _ in range(n):
    temp = list(map(int, input().split()))
    a.append(temp[0])
    b.append(temp[1])
    c.append(temp[2])
Last = -a[-1]
res = []
res.append(Last)
index = len(a)-2
while Last != 0:
    x = a[index]*(Last+1)*num[Last-1]*num[Last-1]+(b[index]+1)*Last*num[Last-1]+c[index]+Last
    y = (Last+1)*num[Last-1]*num[Last-1]+Last*num[Last-1]+1
    Last = int((-1)*x/y)
    index-=1
    res.append(Last)
for i in range(len(res)-2,-1,-1):
    print(res[i])