from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = []
        def dfs(left,right):
            if left+right == 2*n:
                res.append("".join(temp))
                return
            if left<n:
                temp.append("(")
                dfs(left+1,right)
                temp.pop()
            if right<left:
                temp.append(")")
                dfs(left,right+1)
                temp.pop()
        dfs(0,0)
        return res
n = 3
print(Solution().generateParenthesis(n))