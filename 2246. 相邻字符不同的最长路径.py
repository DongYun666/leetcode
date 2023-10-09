from typing import List
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        grid = [[] for _ in range(len(parent))]
        for i in range(1,len(parent)):
            grid[parent[i]].append(i)
        res = 0
        def dfs(i):
            i_length = 0
            for j in grid[i]:
                j_length = dfs(j)
                if s[i] != s[j]:
                    nonlocal res
                    res =  max(res,i_length+j_length+1)
                    i_length = max(i_length,j_length+1)
            return i_length
        dfs(0)
        return res + 1


parent = [-1,0,0,1,1,2]
s = "abacbe"
print(Solution().longestPath(parent,s))