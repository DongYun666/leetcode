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

