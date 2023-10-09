class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        res = max(m,n)
        visted = [[0 for _ in range(m)] for _ in range(n)]
        def dfs(i,j,step):
            nonlocal res
            if step >= res:
                return
            if i >= n:
                res = step
                return
            if j >= m:
                dfs(i+1,0,step)
                return
            if visted[i][j]:
                dfs(i,j+1,step)
                return
            k = min(n-i,m-j)
            while k >= 1 and isAvailable(i,j,k):
                for l in range(i,i+k):
                    for o in range(j,j+k):
                        visted[l][o] = 1
                dfs(i,j+k,step+1)
                for l in range(i,i+k):
                    for o in range(j,j+k):
                        visted[l][o] = 0
                k -= 1
            
        def isAvailable(i,j,k):
            for l in range(i,i+k):
                for o in range(j,j+k):
                    if visted[l][o]:
                        return False
            return True
        dfs(0,0,0)
        return res
    
n = 11
m = 13
print(Solution().tilingRectangle(n,m))