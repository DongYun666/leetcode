# -*- codeing = utf-8 -*-
# @Time : 2022/4/5 14:35
# @Author : DongYun
# @File : 2076.处理含限制条件的好友请求.py
# @Software : PyCharm

from typing import List
class UnionFind:
    def __init__(self,n:int):
        self.parent = list(range(n))
        self.size = [1]*n
        self.n = n
        self.setCount = n
    def findset(self,x:int):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]
    def unite(self,x:int,y:int):
        x,y= self.findset(x),self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x,y = y,x
        self.parent[y] = x
        self.size[x]+=self.size[y]
        self.setCount -=1
        return True
    def connected(self,x:int,y:int):
        x,y = self.findset(x),self.findset(y)
        return x == y
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        ans = []
        for req in requests:
            x,y = uf.findset(req[0]),uf.findset(req[1])
            if x != y:
                check = True
                for res in restrictions:
                    u,v = uf.findset(res[0]),uf.findset(res[1])
                    if (x == u and y == v) or (x == v and y == u):
                        check = False
                        break
                if check:
                    ans.append(True)
                    uf.unite(x,y)
                else:
                    ans.append(False)
            else:
                ans.append(True)
        return ans

n = 5
restrictions = [[0,1],[1,2],[2,3]]
requests = [[0,4],[1,2],[3,1],[3,4]]
print(Solution().friendRequests(n,restrictions,requests))