# -*- codeing = utf-8 -*-
# @Time : 2022/4/25 20:05
# @Author : DongYun
# @File : 美团笔试1.py
# @Software : PyCharm

while True:
    try:
        N,m_p,t_p = list(map(int,input().split()))
        graph = [[] for _ in range(N+1)]
        for i in range(N-1):
            x,y = list(map(int,input().split()))
            graph[x].append(y)
            graph[y].append(x)
        print(graph)
        res_x,res_y = [0]*(N+1),[0]*(N+1)
        def dfs(res,number,time =1):
            res[number] = time
            for i in graph[number]:
                if res[i] == 0:
                    # 以i为起点，继续dfs
                    dfs(res, i, time + 1)
        dfs(res_x,x)
        dfs(res_x,y)
        print(max(res_x[i] - 1 if res_x[i] > res_y[i] else 0 for i in range(N)))
    except:
        break
# 5 1 2
# 2 1
# 3 1
# 4 2
# 5 3