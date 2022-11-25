# -*- codeing = utf-8 -*-
# @Time : 2022/7/23 16:11
# @Author : DongYun
# @File : Seq.py
# @Software : PyCharm
# n,m = list(map(int,input().split()))
# dict = [[1,1,1,1,1]]
# def insert(flag,d):
#     x = d[:temp[0] - 1]
#     if flag == 0:
#         for i in range(temp[0]-1,temp[1]):
#             if d[i] ==0:
#                 x.append(d[i])
#             else:
#                 x.append((d[i]+1)%2)
#     else:
#         for i in range(temp[0]-1,temp[1]):
#             if d[i] ==1:
#                 x.append(d[i])
#             else:
#                 x.append((d[i]+1)%2)
#     x += d[temp[1]:]
#     if x not in dict:
#         res.append(x)
# for _ in range(m):
#     temp = list(map(int, input().split()))
#     res = []
#     for d in dict:
#         insert(0,d)
#         insert(1,d)
#     for r in res:
#         dict.append(r)
# print(dict)
# print(len(dict))



















# def test(x):
#     return x,x+1
# res = test(3)
# print(res)








def hitting(ans,array,command):
    Command = command.copy()
    if command ==[]:
        if array not in ans:
            ans.append(array)
        return ans
    command_i = Command[0]
    l,r = int(command_i[0]-1),int(command_i[1]-1)
    del Command[0]
    array1,array0 = array.copy(),array.copy()
    for i in range(l,r+1):
        array1[i] = 1
        array0[i] = 0
    hitting(ans,array1,Command)
    hitting(ans,array0,Command)
    return ans

def Seq(n,command):
    array = []
    for i in range(n):
        array.append(0)
    ans = []
    ans = hitting(ans,array,command)
    print(len(ans))

def main():
    n,m = map(int,input().split(' '))
    command = []
    for i in range(m):
        l,r = map(int,input().split(' '))
        command.append([l,r])
    # n = 5
    # command = [[1,3],[2,4],[3,4]]
    Seq(n,command)

if __name__ == '__main__':
    exit(main())