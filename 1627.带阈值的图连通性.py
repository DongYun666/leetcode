from typing import List

class UnionFind:
    def __init__(self,n):
        self.father = [i for i in range(n+1)]
    def find(self,x):
        if self.father[x]!=x:
            self.father[x] = self.find(self.father[x])
        return self.father[x]
    def union(self,x,y):
        x_father,y_father = self.find(x),self.find(y)
        if x_father == y_father:
            return
        self.father[y_father] = x_father
    def is_connected(self,x,y):
        return self.find(x) == self.find(y)

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        res = []
        UF = UnionFind(n)
        for i in range(threshold+1,n+1):
            for j in range(1,n//i+1):
                if i*j<=n:
                    UF.union(i,i*j)
        for x,y in queries:
            res.append(UF.is_connected(x,y))
        return res





n = 5
threshold = 1
queries = [[4, 5], [4, 5], [3, 2],[2,3],[3,4]]
print(Solution().areConnected(n, threshold, queries))