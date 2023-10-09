from typing import List
# class Solution:
#     def permutation(self, S: str) -> List[str]:
#         res = []
#         def dfs(s, path):
#             if not s:
#                 res.append(path)
#                 return
#             for i in range(len(s)):
#                 dfs(s[:i]+s[i+1:], path+s[i])
#         dfs(S, "")
#         return list(set(res))
class Solution:
    def permutation(self, S: str) -> List[str]:
        n = len(S)
        res = []
        S = list(S)
        def dfs(index):
            if index == n:
                res.append("".join(S[:]))
            visited = [0 for i in range(26)]
            for i in range(index,n):
                if not visited[ord(S[i])-ord("a")]:
                    visited[ord(S[i])-ord("a")] = 1
                    S[index],S[i] = S[i],S[index]
                    dfs(index+1)
                    S[index],S[i] = S[i],S[index]
        dfs(0)
        return res
S = "qqe"
print(Solution().permutation(S))