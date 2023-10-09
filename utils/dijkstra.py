from collections import defaultdict

grouph = [[0,1,1],
          [0,2,2],
          [0,3,3],
          [1,4,7],
          [1,5,9],
          [2,4,4],
          [3,4,5],
          [3,5,6],
          [4,5,8]
          ]

N = 6
# 转为邻接表
g = defaultdict(list)
for i,j,value in grouph:
    g[i].append([j,value])
    g[j].append([i,value])
distance = [0] * N
visted = [False for _ in range(N)]

def dijkstra(s):  #s 表示一个起点
    distance[s] = 0
