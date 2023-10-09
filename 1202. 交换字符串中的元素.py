from collections import defaultdict
from typing import List

class Solution:
    class UnionFind:
        def __init__(self, n):
            self.father = [i for i in range(n)]

        def find(self, x):
            if self.father[x] != x:
                self.father[x] = self.find(self.father[x])
            return self.father[x]

        def union(self, x, y):
            x_father, y_father = self.find(x), self.find(y)
            if x_father == y_father:
                return
            self.father[y_father] = x_father

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        UF = self.UnionFind(len(s))
        for x,y in pairs:
            UF.union(x,y)

        mp = defaultdict(list)
        for i,c in enumerate(s):
            mp[UF.find(i)].append(c)

        for v in mp.values():
            v.sort()

        res = []
        for i in range(len(s)):
            x = UF.find(i)
            res.append(mp[x][0])
            mp[x].pop(0)
        return "".join(res)

s = "dcab"
pairs = [[0, 3], [1, 2], [0, 2]]
print(Solution().smallestStringWithSwaps(s, pairs))