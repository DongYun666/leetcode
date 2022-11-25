from collections import defaultdict
from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        ans = True
        cnt = defaultdict(list)
        for x,y in dislikes:
            cnt[x].append(y)
            cnt[y].append(x)
        color = [-1]*(n+1)
        def dfs(x,c):
            nonlocal ans
            if not ans:
                return
            color[x] = c
            for y in cnt[x]:
                if color[y] != -1:
                    if color[y] == c:
                        ans = False
                        return
                else:
                    dfs(y,1-c)

        for i in range(1,n+1):
            if color[i] == -1:
                dfs(i,1)
        return ans

    def possibleBipartition2(self, n: int, dislikes: List[List[int]]) -> bool:
        cnt = defaultdict(list)
        for x,y in dislikes:
            cnt[x].append(y)
            cnt[y].append(x)
        color = [0]*(n+1)
        for i in range(1,n+1):
            if color[i] == 0:
                q = [i]
                color[i] = 1
                while len(q) != 0:
                    x = q.pop(0)
                    for y in cnt[x]:
                        if color[y] == color[x]:
                            return False
                        if color[y] == 0:
                            color[y] = -color[x]
                            q.append(y)
        return True
    def possibleBipartition3(self, n: int, dislikes: List[List[int]]) -> bool:
        cnt = defaultdict(list)
        for x, y in dislikes:
            cnt[x].append(y)
            cnt[y].append(x)
        U_F = UnionFind(n)
        for x,nodes in cnt.items():
            for y in nodes:
                U_F.union(nodes[0],y)
                if U_F.is_connected(x,y):
                    return False
        return True

class UnionFind:
    def __init__(self,n):
        self.father = [i for i in range(n+1)]
        self.rank = [1]*(n+1)
    def find(self,x):
        if self.father[x]!=x:
            self.father[x] = self.find(self.father[x])
        return self.father[x]
    def union(self,x,y):
        x_father,y_father = self.find(x),self.find(y)
        if x_father == y_father:
            return
        if self.rank[x_father]<self.rank[y_father]:
            x_father,y_father = y_father,x_father
        self.rank[x_father]+=self.rank[y_father]
        self.father[y_father] = x_father
    def is_connected(self,x,y):
        return self.find(x) == self.find(y)









n = 4
dislikes = [[1, 2], [1, 3], [2, 4]]

# n = 5
# dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
print(Solution().possibleBipartition3(n,dislikes))