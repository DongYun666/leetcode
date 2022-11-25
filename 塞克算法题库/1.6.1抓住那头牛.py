# -*- codeing = utf-8 -*-
# @Time : 2022/7/16 10:51
# @Author : DongYun
# @File : 1.6.1抓住那头牛.py
# @Software : PyCharm
N,K = list(map(int,input().split()))
visit = [0]*(max(N,K)*max(N,K)+1)
q = []
q.append(N)
while len(q)!=0:
    cur = q.pop(0)
    if cur == K:
        break
    temp = []
    temp.append(cur-1)
    temp.append(cur+1)
    temp.append(2*cur)
    for i in range(len(temp)):
        if 0<=temp[i]<=100001 and visit[temp[i]]==0:
            q.append(temp[i])
            visit[temp[i]] = visit[cur]+1
print(visit[K])


