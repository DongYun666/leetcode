from typing import List
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        a = []
        mod = 10**9+7
        while n:
            temp = n
            n = n & (n-1)
            a.append(temp ^ n)
        # 求前缀积
        for i in range(1,len(a)):
            a[i] = (a[i] * a[i-1]) % mod
        # 求区间积
        res = []
        for left,right in queries:
            res.append((a[right]//(a[left-1] if left > 0 else 1)%mod))
        return res
    

        print(a)
n = 15
queries = [[0,1],[2,2],[0,3]]

# n = 2
# queries = [[0,0]]

print(Solution().productQueries(n,queries))