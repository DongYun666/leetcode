from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        temp = []
        def dfs(cur,n,k):
            if len(temp)+(n-cur+1)<k:
                return
            if len(temp) == k:
                res.append(temp[:])
                return
            temp.append(cur)
            dfs(cur+1,n,k)
            temp.pop()
            dfs(cur+1,n,k)

        dfs(1,n,k)
        return res
n = 4
k = 2
print(Solution().combine(n, k))