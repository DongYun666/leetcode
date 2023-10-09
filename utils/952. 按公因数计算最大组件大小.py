from collections import Counter
from typing import List

class UnionFind:
    def __init__(self,n):
        self.father = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)

    def find(self,x):
        if self.father[x]!=x:
            self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def union(self,x,y):
        x_father,y_father = self.find(x),self.find(y)
        
        if x_father == y_father:
            return
        
        # if self.rank[x_father]>self.rank[y_father]:
        #     self.father[y_father] = x_father
        # elif self.rank[x_father]<self.rank[y_father]:
        #     self.father[x_father] = y_father
        # else:
        #     self.father[y_father] = x_father
        #     self.rank[x_father]+=1
        if self.rank[x_father]<self.rank[y_father]:
            x_father,y_father = y_father,x_father
        self.rank[x_father]+=self.rank[y_father]
        self.father[y_father] = x_father

    def is_connected(self,x,y):
        return self.find(x) == self.find(y)

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        uf = UnionFind(max(nums))
        for num in nums:
            i = 2
            while i * i <= num:
                if num % i == 0:
                    uf.union(num,i)
                    uf.union(num,num//i)
                i += 1
        return max(Counter(uf.find(num) for num in nums).values())

nums = [4,6,15,35]
# nums = [2,3,6,7,4,12,21,39]
nums = [51,35,40,83,20,88,57,26,30]
print(Solution().largestComponentSize(nums))
