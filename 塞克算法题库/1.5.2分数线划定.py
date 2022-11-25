# -*- codeing = utf-8 -*-
# @Time : 2022/7/15 23:04
# @Author : DongYun
# @File : 1.5.2分数线划定.py
# @Software : PyCharm
import functools


def cmp(a,b):
    if a.s != b.s:
        return a.s-b.s
    if a.id!=b.id:
        return b.id - a.id

class Score:
    def __init__(self,id,s,pos):
        self.id = id
        self.s = s
        self.pos = pos
n,m = list(map(int,input().split()))
score_list = []
for i in range(n):
    temp = list(map(int,input().split()))
    score_list.append(Score(temp[0],temp[1],i))
score_list = sorted(score_list,key=functools.cmp_to_key(cmp),reverse=True)
top = 1
max_score = score_list[0].s
score_list[0].pos = 1
line_score = score_list[0].s
count=1
for i in range(1,len(score_list)):
    if score_list[i].s != max_score:
        score_list[i].pos = i+1
        max_score = score_list[i].s
    else:
        score_list[i].pos = score_list[i-1].pos
    if score_list[i].pos <= int(m*1.5):
        count+=1
        line_score = score_list[i].s
print(line_score,count)
for i in range(count):
    print(score_list[i].id,score_list[i].s)
