# -*- codeing = utf-8 -*-
# @Time : 2022/4/29 20:25
# @Author : DongYun
# @File : 美团2021春招笔试4.py
# @Software : PyCharm
while True:
    try:
        N = int(input())
        nodes = list(map(int,input().split()))
        node_map = []
        for i in range(N):
            temp = []
            for j in range(N):
                if i == j:
                    temp.append(float("inf"))
                else:
                    temp.append(nodes[i]*nodes[j])
            node_map.append(temp)
        vis = [0]*N #表示是否遍历过
        res = 0
        for i in range(N):
            res += min(node_map[i])


        print(node_map)
    except:
        break

