from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def dfs(s,sub):
            if len(sub) == 4:
                if not s:
                    res.append('.'.join(sub))
                return
            for i in range(1,4):
                if i <= len(s):
                    if s[0] == '0' and i > 1:
                        break
                    if int(s[:i]) <= 255:
                        dfs(s[i:],sub+[s[:i]])
                    
        dfs(s, [])
        return res
s = "25525511135"
s = "0000"
s = "101023"
print(Solution().restoreIpAddresses(s))
