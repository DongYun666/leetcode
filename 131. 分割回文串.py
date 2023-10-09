from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        path = []
        def ispalindrome(start,end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        def dfs(index):
            if index == n:
                res.append(path[:])
                return
            for i in range(index,n):
                if ispalindrome(index,i):
                    path.append(s[index:i+1])
                    dfs(i+1)
                    path.pop()
        dfs(0)
        return res
s = "aab"
print(Solution().partition(s))