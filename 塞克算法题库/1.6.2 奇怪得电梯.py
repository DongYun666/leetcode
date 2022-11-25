# -*- codeing = utf-8 -*-
# @Time : 2022/7/16 17:53
# @Author : DongYun
# @File : 1.6.2 奇怪得电梯.py
# @Software : PyCharm
class Point:
    def __init__(self,x,step):
        self.x = x
        self.step = step

N,A,B = list(map(int,input().split()))
num = list(map(int,input().split()))
num.insert(0,0)
visited = [0]*(N+1)
visited[num[A]] = 1
q = []
q.append(Point(A,0))
res = -1
while len(q) > 0:
    cur = q.pop(0)
    if cur.x == B:
        res = cur.step
        break
    next_point = Point(cur.x+num[cur.x],0)
    if 0<next_point.x<=N and visited[next_point.x] != 1:
        visited[next_point.x] = 1
        next_point.step = cur.step+1
        q.append(next_point)
    next_point = Point(cur.x - num[cur.x], 0)
    if 0<next_point.x <= N and visited[next_point.x] != 1:
        visited[next_point.x] = 1
        next_point.step = cur.step + 1
        q.append(next_point)
print(res if res != -1 else -1)