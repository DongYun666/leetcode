from typing import List

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x: x[2])

        fa = list(range(n))
        def find(x):
            if fa[x]!= x:
                fa[x] = find(fa[x])
            return fa[x]
        def merge(x,y):
            fa[find(x)] = find(y)

        ans,k = [False]*len(queries),0
        for i,(p,q,limit) in sorted(enumerate(queries),key=lambda x:x[1][2]):
            while k < len(edgeList) and edgeList[k][2] < limit:
                merge(edgeList[k][0],edgeList[k][1])
                k += 1
            ans[i] = find(p) == find(q)
        return ans


n = 5
edgeList = [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]]
queries = [[0, 4, 14], [1, 4, 13]]
print(Solution().distanceLimitedPathsExist(n, edgeList, queries))