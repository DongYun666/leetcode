from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def issub(s,t):
            s_i,t_i = 0,0
            while s_i < len(s) and t_i < len(t):
                if s[s_i] == t[t_i]:
                    s_i+=1
                t_i+=1
            return s_i == len(s)
        ans = -1
        for i,s in enumerate(strs):
            flag = True
            for j,t in enumerate(strs):
                if i!=j and issub(s,t):
                    flag = False
                    break
            if flag:
                ans = max(ans,len(s))
        return ans


strs = ["aba", "cdc", "eae"]
# strs = ["aabbcc", "aabbcc","c"]
print(Solution().findLUSlength(strs))