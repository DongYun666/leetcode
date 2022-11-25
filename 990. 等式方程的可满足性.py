from typing import List

class UnionFind:
    def __init__(self):
        self.father = [i for i in range(26)]
        self.rank = [1]*26
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

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        UF = UnionFind()
        for equation in equations:
            a,b,eq = equation[0],equation[3],equation[1]
            if eq == "=":
                UF.union(ord(a)-ord("a"),ord(b)-ord("a"))
        for equation in equations:
            a, b, eq = equation[0], equation[3], equation[1]
            if eq == "!":
                if UF.is_connected(ord(a)-ord("a"),ord(b)-ord("a")):
                    return False
        return True


equations = ["a==b", "b==c", "c!=d"]
equations = ["a==b","b!=c","c==a"]
equations = ["c==c","b==d","x!=z"]
print(Solution().equationsPossible(equations))