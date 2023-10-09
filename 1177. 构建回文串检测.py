from collections import Counter
from typing import List
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        res = []
        def check(l,r,k):
            cnt = Counter(s[l:r + 1])
            ans = 0
            for w,c in cnt.items():
                if c % 2:
                    ans += 1
            if len(s[l:r + 1]) % 2:
                ans -= 1
            return ans//2 <= k
        for left,right,k in queries:
            if check(left,right,k):
                res.append(True)
            else:
                res.append(False)
        return res


s = "abcda"
queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]

# s = "lyb"
# queries = [[0,1,0],[2,2,1]]
s = "hunu"
queries = [[1,1,1],[2,3,0],[3,3,1],[0,3,2],[1,3,3],[2,3,1],[3,3,1],[0,3,0],[1,1,1],[2,3,0],[3,3,1],[0,3,1],[1,1,1]]

print(Solution().canMakePaliQueries(s,queries))