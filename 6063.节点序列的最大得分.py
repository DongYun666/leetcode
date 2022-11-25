# -*- codeing = utf-8 -*-
# @Time : 2022/4/17 20:08
# @Author : DongYun
# @File : 6063.节点序列的最大得分.py
# @Software : PyCharm
from heapq import nlargest
from itertools import product
from typing import List
# class Solution:
#     def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
#         res = []
#         temp = set()
#         count = 0
#         for i in range(len(scores)):
#             if i+1 < len(scores):
#                 if [i,i+1] in edges:
#                     temp.add(i)
#                     temp.add(i+1)
#                     count+=1
#                 else:
#                     count = 0
#                     if len(temp) > 3:
#                         res.append(list(temp))
#                     temp.clear()
#         if len(temp)>3:
#             res.append(list(temp))
#         print(res)
#         if len(res) == 0:
#             return -1
#         ans = 0
#         for r in res:
#             sc = []
#             for index in range(len(r)):
#                 sc.append(scores[index])
#             sc+=sc
#             for index in range(len(sc)-4):
#                 ans = max(ans,sum(sc[index:index+4]))
#         return ans
class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        g = [[] for _ in range(len(scores))]
        for x, y in edges:
            g[x].append((scores[y], y))
            g[y].append((scores[x], x))
        print(g)
        for i, vs in enumerate(g):
            g[i] = nlargest(3, vs)
        print(g)
        # 下面这一段可以简写成一行，为了可读性这里就不写了
        ans = -1
        for x, y in edges:
            print(x,y)
            print("----------")
            for (score_a, a), (score_b, b) in product(g[x], g[y]):
                print((score_a, a), (score_b, b))
                if y != a != b != x:
                    ans = max(ans, score_a + scores[x] + scores[y] + score_b)
        return ans

scores = [16,21,22,2,24,21,12,17,2,24]

edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,0]]
print(Solution().maximumScore(scores,edges))
