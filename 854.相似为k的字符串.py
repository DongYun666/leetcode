class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        # 保留位置不同时的情况
        s1_temp,s2_temp = [],[]
        for x,y in zip(s1,s2):
            if x!=y:
                s1_temp.append(x)
                s2_temp.append(y)
        n = len(s1_temp)
        if n == 0:
            return 0
        ans = n-1
        def dfs(cur,r):
            nonlocal ans
            if r > ans:
                return
            while cur <n and s1_temp[cur] == s2_temp[cur]:
                cur+=1
            if cur == n:
                ans = min(ans,r)
                return
            diff = sum(s1_temp[j]!= s2_temp[j] for j in range(cur,n))
            min_swap = (diff+1)//2
            if r+min_swap >=ans:
                return
            for j in range(cur+1,n):
                if s1_temp[j] == s2_temp[cur]:
                    s1_temp[cur],s1_temp[j] = s1_temp[j],s1_temp[cur]
                    dfs(cur+1,r+1)
                    s1_temp[cur],s1_temp[j] = s1_temp[j],s1_temp[cur]
        dfs(0,0)
        return ans


s1 = "abca"
s2 = "baac"
print(Solution().kSimilarity(s1, s2))