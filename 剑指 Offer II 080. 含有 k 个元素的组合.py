from itertools import combinations
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1,n+1), k))
    def combine2(self, n: int, k: int) -> List[List[int]]:
        ans,temp = [],[]
        def dfs(cur,n,k):
            if len(temp)+(n-cur+1)<k:
                return
            if len(temp) == k:
                ans.append(temp[:])
                return
            temp.append(cur)
            dfs(cur+1,n,k)
            temp.pop()
            dfs(cur+1,n,k)
        dfs(1,n,k)
        return ans

n = 4
k = 2
print(Solution().combine2(n, k))